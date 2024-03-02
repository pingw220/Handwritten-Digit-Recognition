from flask import Flask, request, jsonify, render_template_string
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

# Initialize Flask app
app = Flask(__name__)

# Load your pre-trained model
model = load_model('mnist_model.h5')

# Define a route for the homepage
@app.route('/')
def home():
    return render_template_string('''
        <h1>Digit Recognition</h1>
        <p>Upload a PNG, JPG, or JPEG image of a handwritten digit.</p>
        <form action="/predict" method="post" enctype="multipart/form-data">
            <input type="file" name="file" />
            <input type="submit" value="Upload and Predict" />
        </form>
    ''')

# Define a route for processing uploaded images and making predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and (file.filename.endswith('.png') or file.filename.endswith('.jpg') or file.filename.endswith('.jpeg')):
        # Convert the image to grayscale (MNIST images are grayscale)
        img.save("debug_preprocessed.png")
        img = Image.open(file.stream).convert('L')
        
        # Resize the image to 28x28 pixels (the size used by MNIST)
        img = img.resize((28, 28))
        
        # Convert the image to a numpy array and normalize it
        img_array = np.array(img) / 255.0
        # Reshape the array for the model (adding batch dimension and channel dimension)
        img_array = img_array.reshape((1, 28, 28, 1))
        # Make a prediction
        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        img_array = img_array.reshape((1, 28, 28, 1))  # Correct shape for the model
        # Return the prediction
        return jsonify({'predicted_digit': int(predicted_digit)})

    return jsonify({'error': 'Invalid file format. Please upload a PNG, JPG, or JPEG file.'})

if __name__ == '__main__':
    app.run(debug=True)
