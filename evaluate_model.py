"""
Model Evaluation Script for Rice Classification
This script evaluates the model performance on test data and generates detailed metrics.
"""

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from PIL import Image
import os
from pathlib import Path
import keras

# Enable unsafe deserialization for Lambda layers
keras.config.enable_unsafe_deserialization()

# Rice class names
class_names = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

def load_model():
    """Load the trained rice classification model"""
    try:
        model = tf.keras.models.load_model('rice.keras', custom_objects={'KerasLayer': hub.KerasLayer})
        # Patch Lambda layers to ensure they have access to required globals
        for layer in model.layers:
            if isinstance(layer, tf.keras.layers.Lambda):
                layer.function.__globals__['hub'] = hub
                layer.function.__globals__['mobile_net'] = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def preprocess_image(image_path, target_size=(224, 224)):
    """Preprocess image for model prediction"""
    try:
        img = Image.open(image_path).convert('RGB')
        img = img.resize(target_size)
        img_array = np.array(img) / 255.0
        return np.expand_dims(img_array, axis=0)
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def load_test_data(test_dir="test_data", max_samples_per_class=50):
    """Load test data from the test_data directory"""
    images = []
    labels = []
    image_paths = []
    
    for class_idx, class_name in enumerate(class_names):
        class_path = Path(test_dir) / class_name
        if not class_path.exists():
            print(f"Warning: Directory {class_path} not found")
            continue
            
        image_files = list(class_path.glob("*.jpg"))[:max_samples_per_class]
        print(f"Loading {len(image_files)} images for {class_name}")
        
        for img_path in image_files:
            processed_img = preprocess_image(img_path)
            if processed_img is not None:
                images.append(processed_img[0])  # Remove batch dimension
                labels.append(class_idx)
                image_paths.append(str(img_path))
    
    return np.array(images), np.array(labels), image_paths

def evaluate_model():
    """Main evaluation function"""
    print("Loading model...")
    model = load_model()
    if model is None:
        return
    
    print("Loading test data...")
    X_test, y_test, image_paths = load_test_data()
    
    if len(X_test) == 0:
        print("No test data found!")
        return
    
    print(f"Loaded {len(X_test)} test images")
    print(f"Class distribution: {np.bincount(y_test)}")
    
    # Make predictions
    print("Making predictions...")
    predictions = model.predict(X_test)
    y_pred = np.argmax(predictions, axis=1)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nOverall Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    # Classification report
    print("\nClassification Report:")
    report = classification_report(y_test, y_pred, target_names=class_names)
    print(report)
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    # Plot confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Per-class accuracy
    per_class_accuracy = cm.diagonal() / cm.sum(axis=1)
    
    print("\nPer-class Accuracy:")
    for i, class_name in enumerate(class_names):
        print(f"{class_name}: {per_class_accuracy[i]:.4f} ({per_class_accuracy[i]*100:.2f}%)")
    
    # Find misclassified examples
    print("\nAnalyzing misclassifications...")
    misclassified_indices = np.where(y_test != y_pred)[0]
    
    if len(misclassified_indices) > 0:
        print(f"Found {len(misclassified_indices)} misclassified images:")
        
        # Show first 5 misclassifications
        for i, idx in enumerate(misclassified_indices[:5]):
            true_label = class_names[y_test[idx]]
            pred_label = class_names[y_pred[idx]]
            confidence = predictions[idx][y_pred[idx]]
            print(f"  {i+1}. {image_paths[idx]}")
            print(f"     True: {true_label}, Predicted: {pred_label} (Confidence: {confidence:.3f})")
    
    # Save results
    results = {
        'accuracy': accuracy,
        'classification_report': report,
        'confusion_matrix': cm.tolist(),
        'per_class_accuracy': per_class_accuracy.tolist(),
        'class_names': class_names
    }
    
    # Create a summary DataFrame
    results_df = pd.DataFrame({
        'Rice Type': class_names,
        'Accuracy': per_class_accuracy,
        'Samples': cm.sum(axis=1)
    })
    
    print("\nSummary:")
    print(results_df)
    
    # Save to CSV
    results_df.to_csv('model_evaluation_results.csv', index=False)
    print("\nResults saved to 'model_evaluation_results.csv'")
    print("Confusion matrix saved to 'confusion_matrix.png'")

if __name__ == "__main__":
    evaluate_model()
