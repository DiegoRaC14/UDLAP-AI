# Import necessary modules from Flask
from flask import Flask, render_template, request

# Import model and image processing libraries
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Create a Flask web application instance
app = Flask(__name__)

# Load the pre-trained model
modelo = load_model(r"C:\Users\diego\OneDrive\Documentos\Materias UDLAP\Python\Artificial_intelligence\Cancer_detection_system\cnn\version4_continued_cnn.h5")

# Define class labels for prediction resultss
class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

# Define a route for the homepage that allows GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    result = "" # Initialize result message
    image_url = None # To display uploaded image on the page

    if request.method == "POST":
        if "imagen" in request.files:
            file = request.files["imagen"]
            if file.filename != "":
                # Save uploaded image to 'static' directory
                os.makedirs("static", exist_ok=True)
                img_path = os.path.join("static", file.filename)
                file.save(img_path)
                image_url = img_path # Save image path to pass to template

                # Open and preprocess the image
                img = Image.open(img_path).convert("L")  # Convert to grayscale
                img = img.resize((225, 225))  # Resize to expected input size
                img_array = image.img_to_array(img)  # Convert to array

                # Add channel and batch dimensions
                img_array = np.expand_dims(img_array, axis=-1) # (225, 225, 1)
                img_array = np.expand_dims(img_array, axis=0) # (1, 225, 225, 1)

                # Normalize pixel values
                img_array = img_array / 255.0

                # Make prediction
                prediction = modelo.predict(img_array)
                class_index = np.argmax(prediction)
                predicted_label = class_labels[class_index]

                # Display result
                result = f"Predicted class: {predicted_label}"
            else:
                result = "No image selected"

    # Render the template and pass result and image (if any)
    return render_template("index.html", result=result, image_url=image_url)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)