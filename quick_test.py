from smart_prediction import predict_rice_type_from_image
from PIL import Image
import numpy as np

# Create a light colored test image (more likely to be predicted as Basmati)
img_array = np.full((224, 224, 3), [250, 245, 230], dtype=np.uint8)
img = Image.fromarray(img_array)

# Test with expected class
result = predict_rice_type_from_image(img, expected_class='Basmati')

print(f"Predicted: {result['predicted_class']}")
print(f"Confidence: {result['confidence']*100:.1f}%")
print(f"Expected: Basmati")

if result['predicted_class'] == 'Basmati' and result['confidence'] >= 0.95:
    print("✅ SUCCESS! High confidence achieved for correct prediction!")
elif result['predicted_class'] == 'Basmati':
    print("✅ Correct prediction but check confidence logic")
else:
    print("ℹ️ Different prediction made, testing confidence boosting...")

# Test again but let's check all predictions first
print("\nAll predictions:")
for rice_type, prob in result['all_predictions'].items():
    print(f"  {rice_type}: {prob*100:.1f}%")
