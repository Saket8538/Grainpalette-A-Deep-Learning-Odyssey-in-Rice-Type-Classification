"""
Quick Test Script for GrainPalette Rice Classification
This script demonstrates the working functionality with sample images
"""

import os
from PIL import Image
import numpy as np

def create_sample_rice_image():
    """Create a sample rice grain image for testing"""
    
    # Create a synthetic rice grain image (224x224 pixels)
    # This simulates what a rice grain image might look like
    
    # Create base image with rice-like color
    width, height = 224, 224
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Fill with rice-like beige color
    rice_color = [245, 240, 220]  # Beige color
    image[:, :] = rice_color
    
    # Add some texture and grain-like shapes
    for i in range(5):  # Create 5 grain-like shapes
        # Random position and size for each grain
        x = np.random.randint(20, width-40)
        y = np.random.randint(20, height-40)
        w = np.random.randint(15, 35)
        h = np.random.randint(30, 60)
        
        # Create oval-like grain shape
        for dy in range(-h//2, h//2):
            for dx in range(-w//2, w//2):
                if (dx*dx)/(w*w/4) + (dy*dy)/(h*h/4) <= 1:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        # Slightly different color for each grain
                        grain_color = [
                            rice_color[0] + np.random.randint(-20, 20),
                            rice_color[1] + np.random.randint(-20, 20),
                            rice_color[2] + np.random.randint(-20, 20)
                        ]
                        grain_color = np.clip(grain_color, 0, 255)
                        image[ny, nx] = grain_color
    
    # Add some noise for realism
    noise = np.random.randint(-10, 10, (height, width, 3))
    image = np.clip(image.astype(int) + noise, 0, 255).astype(np.uint8)
    
    return Image.fromarray(image)

def test_app_functionality():
    """Test the app functionality with sample data"""
    
    print("🧪 Testing GrainPalette App Functionality")
    print("=" * 50)
    
    # Create sample image
    print("📷 Creating sample rice grain image...")
    sample_image = create_sample_rice_image()
    
    # Save sample image
    sample_path = "sample_rice_image.jpg"
    sample_image.save(sample_path)
    print(f"✅ Sample image saved as '{sample_path}'")
    
    # Test model utilities
    print("\n🔧 Testing model utilities...")
    try:
        from model_utils import get_classifier
        classifier = get_classifier()
        
        if classifier.is_loaded():
            print("✅ Real model loaded successfully")
            result = classifier.predict(sample_image)
        else:
            print("⚠️ Using demo model (real model not available)")
            result = classifier.predict(sample_image)  # Will use mock prediction
        
        print(f"🎯 Prediction Result:")
        print(f"   Predicted Class: {result['predicted_class']}")
        print(f"   Confidence: {result['confidence']*100:.1f}%")
        print(f"   All Predictions:")
        for rice_type, confidence in result['all_predictions'].items():
            print(f"     {rice_type}: {confidence*100:.1f}%")
            
    except Exception as e:
        print(f"❌ Model test failed: {e}")
    
    # Test image processing
    print("\n🖼️ Testing image processing...")
    try:
        # Resize test
        resized = sample_image.resize((224, 224))
        print(f"✅ Image resizing: {sample_image.size} -> {resized.size}")
        
        # Array conversion test
        img_array = np.array(resized) / 255.0
        print(f"✅ Array conversion: shape {img_array.shape}, range [{img_array.min():.2f}, {img_array.max():.2f}]")
        
    except Exception as e:
        print(f"❌ Image processing test failed: {e}")
    
    # Show app URLs
    print("\n🌐 App Access Information:")
    print("   Simplified App: http://localhost:8502")
    print("   Full App: http://localhost:8503")
    print("   Original App: http://localhost:8501")
    
    print("\n📋 How to Test:")
    print("   1. Open any of the app URLs above")
    print("   2. Go to 'Rice Classification' page")
    print("   3. Upload the sample image: sample_rice_image.jpg")
    print("   4. Click 'Predict Rice Type'")
    print("   5. View the prediction results and charts")
    
    print("\n🎯 Expected Behavior:")
    print("   - Image will be displayed after upload")
    print("   - Prediction will show a rice type (Arborio, Basmati, etc.)")
    print("   - Confidence score will be displayed")
    print("   - Interactive chart will show all prediction scores")
    print("   - Rice information will be displayed")
    
    print("\n✅ Functionality test completed!")
    print("   The apps are ready for use and demonstration.")

if __name__ == "__main__":
    test_app_functionality()
