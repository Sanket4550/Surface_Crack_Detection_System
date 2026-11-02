
import os
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

IMAGE_SIZE = 128

# Load trained CNN model
model = load_model("Best_Crack_Detection_Model.keras")

def predict_single_image(image_path):

    if not os.path.exists(image_path):
        print("Image not found:", image_path)
        return

    # Load and preprocess image
    img = load_img(image_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))

    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array, verbose=0)[0][0]

    # Class indices: Crack = 0, NoCrack = 1
    if prediction > 0.5:
        result = "No Crack"
    else:
        result = "Crack Detected"

    print("=" * 50)
    print("CRACK DETECTION RESULT")
    print("=" * 50)
    print("Image:", image_path)
    print("Prediction Score:", prediction)
    print("Result:", result)

    # Display image and prediction
    plt.imshow(img)
    plt.title(result)
    plt.axis("off")
    plt.show()


# Test your new image here
image_folder = "New_Images"

for image in os.listdir(image_folder):

    if image.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):

        image_path = os.path.join(image_folder, image)

        predict_single_image(image_path)
