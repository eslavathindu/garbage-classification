import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load model
model = load_model('model.h5')

# Class names
class_names = ['plastic', 'paper', 'metal', 'glass']

# Get image path
img_path = input("Enter full path of the garbage image: ")

# Load and preprocess
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array)
predicted_class = class_names[np.argmax(prediction)]

print(f"\n🧠 Predicted Garbage Type: {predicted_class.upper()}")
