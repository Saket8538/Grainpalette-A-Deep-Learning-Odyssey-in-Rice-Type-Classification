"""
Test Script for Rice Classification App
This script tests various components of the rice classification system.
"""

import os
import sys
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import keras
from model_utils import get_classifier

# Enable unsafe deserialization for Lambda layers
keras.config.enable_unsafe_deserialization()

def test_model_loading():
    """Test if the model can be loaded successfully"""
    print("🧪 Testing model loading...")
    try:
        classifier = get_classifier()
        if classifier.is_loaded():
            print("✅ Model loaded successfully!")
            print(f"   Supported classes: {', '.join(classifier.class_names)}")
            return classifier
        else:
            print("❌ Model failed to load")
            return None
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None

def test_single_prediction(classifier, image_path):
    """Test prediction on a single image"""
    print(f"\n🧪 Testing prediction on {image_path}...")
    try:
        result = classifier.predict(image_path)
        
        print(f"✅ Prediction successful!")
        print(f"   Predicted class: {result['predicted_class']}")
        print(f"   Confidence: {result['confidence']*100:.2f}%")
        
        # Show all predictions
        print("   All predictions:")
        for class_name, prob in result['all_predictions'].items():
            print(f"     {class_name}: {prob*100:.2f}%")
        
        return True
    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return False

def test_batch_prediction(classifier, test_dir="test_data", samples_per_class=3):
    """Test predictions on multiple images"""
    print(f"\n🧪 Testing batch predictions...")
    
    class_names = classifier.class_names
    total_correct = 0
    total_tested = 0
    
    for class_idx, class_name in enumerate(class_names):
        class_path = os.path.join(test_dir, class_name)
        if not os.path.exists(class_path):
            print(f"⚠️  Directory {class_path} not found, skipping...")
            continue
        
        # Get sample images
        image_files = [f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        sample_files = image_files[:samples_per_class]
        
        class_correct = 0
        for img_file in sample_files:
            img_path = os.path.join(class_path, img_file)
            try:
                result = classifier.predict(img_path)
                predicted_class = result['predicted_class']
                
                if predicted_class == class_name:
                    class_correct += 1
                
                total_tested += 1
                
            except Exception as e:
                print(f"❌ Error processing {img_path}: {e}")
        
        total_correct += class_correct
        accuracy = class_correct / len(sample_files) if sample_files else 0
        print(f"   {class_name}: {class_correct}/{len(sample_files)} correct ({accuracy*100:.1f}%)")
    
    overall_accuracy = total_correct / total_tested if total_tested > 0 else 0
    print(f"\n✅ Overall test accuracy: {total_correct}/{total_tested} ({overall_accuracy*100:.1f}%)")
    
    return overall_accuracy

def test_requirements():
    """Test if all required packages are installed"""
    print("🧪 Testing requirements...")
    
    required_packages = [
        'streamlit',
        'tensorflow',
        'tensorflow_hub',
        'pillow',
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'plotly'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'pillow':
                import PIL
            elif package == 'tensorflow_hub':
                import tensorflow_hub
            else:
                __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - NOT INSTALLED")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("   Install with: pip install " + " ".join(missing_packages))
        return False
    else:
        print("✅ All required packages are installed!")
        return True

def test_file_structure():
    """Test if all required files are present"""
    print("🧪 Testing file structure...")
    
    required_files = [
        'rice.keras',
        'app.py',
        'requirements.txt',
        'README.md'
    ]
    
    optional_files = [
        'main.py',
        'predict.py',
        'team_images/',
        'test_data/'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - NOT FOUND")
            missing_files.append(file_path)
    
    for file_path in optional_files:
        if os.path.exists(file_path):
            print(f"   ✅ {file_path} (optional)")
        else:
            print(f"   ⚠️  {file_path} - NOT FOUND (optional)")
    
    if missing_files:
        print(f"\n⚠️  Missing required files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files are present!")
        return True

def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Rice Classification System Tests")
    print("=" * 50)
    
    # Test file structure
    structure_ok = test_file_structure()
    
    # Test requirements
    requirements_ok = test_requirements()
    
    if not (structure_ok and requirements_ok):
        print("\n❌ Basic requirements not met. Please fix the issues above.")
        return False
    
    # Test model loading
    model = test_model_loading()
    if model is None:
        print("\n❌ Cannot proceed without a working model.")
        return False
    
    # Test single prediction (use any available test image)
    test_image_found = False
    for class_name in model.class_names:
        test_dir = os.path.join('test_data', class_name)
        if os.path.exists(test_dir):
            test_images = [f for f in os.listdir(test_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            if test_images:
                test_image_path = os.path.join(test_dir, test_images[0])
                test_single_prediction(model, test_image_path)
                test_image_found = True
                break
    
    if not test_image_found:
        print("\n⚠️  No test images found for single prediction test")
    
    # Test batch predictions
    if os.path.exists('test_data'):
        test_batch_prediction(model)
    else:
        print("\n⚠️  No test_data directory found for batch testing")
    
    print("\n" + "=" * 50)
    print("🎉 Testing completed!")
    print("\nTo run the Streamlit app, use:")
    print("   streamlit run app.py")
    
    return True

if __name__ == "__main__":
    run_all_tests()
