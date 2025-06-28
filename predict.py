# predict.py

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import keras
import numpy as np
import os
import warnings

warnings.filterwarnings("ignore")

# Make sure 'hub' is available globally
globals()["hub"] = hub

# Define mobile_net and add to global namespace
mobile_net = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
globals()["mobile_net"] = mobile_net

# Rice class names
class_names = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

try:
    model = load_model('rice.keras', custom_objects={'KerasLayer': hub.KerasLayer})
    # Patch Lambda layers to ensure they have access to required globals
    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.Lambda):
            layer.function.__globals__['hub'] = hub
            layer.function.__globals__['mobile_net'] = mobile_net
    print("Model loaded successfully from rice.keras")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

def predict_rice_type(image_path):
    """
    Predicts the rice type from an image path using the loaded model.

    Args:
        image_path (str): Path to the image file.

    Returns:
        predicted_label (str): Predicted rice type label.
        prediction_probability (float): Probability of the predicted class.
    """
    try:
        # Load and preprocess the image
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.  # Rescale pixel values to [0, 1]

        # Perform prediction
        prediction = model.predict(img_array)
        predicted_class_index = np.argmax(prediction)
        predicted_label = class_names[predicted_class_index]
        prediction_probability = prediction[0][predicted_class_index]

        return predicted_label, prediction_probability

    except Exception as e:
        print(f"Error during prediction: {e}")
        return None, None

if __name__ == '__main__':
    # Standalone test usage
    test_image_path = '/content/rice_dataset_split/test/Jasmine/Jasmine (10029).jpg'

    if not os.path.exists(test_image_path):
        print(f"Error: Image file not found at path: {test_image_path}")
    else:
        predicted_label, prediction_probability = predict_rice_type(test_image_path)
        if predicted_label:
            print(f"Predicted Rice Type: {predicted_label}")
            print(f"Probability: {prediction_probability:.4f}")
        else:
            print("Prediction failed.")
