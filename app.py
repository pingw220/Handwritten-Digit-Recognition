from flask import Flask, request, jsonify, render_template_string
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2

app = Flask(__name__)
model = load_model('mnist_model.h5')  # Ensure the path is correct

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

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and (file.filename.endswith('.png') or file.filename.endswith('.jpg') or file.filename.endswith('.jpeg')):
        img = Image.open(file.stream).convert('L')  # Convert to grayscale
        
        # Convert PIL image to OpenCV format
        img_cv = np.array(img)
        
        # Apply adaptive thresholding to create a binary image
        thresh = cv2.adaptiveThreshold(img_cv, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                       cv2.THRESH_BINARY, 11, 2)
        
        # Invert the image colors to match the MNIST format
        thresh = cv2.bitwise_not(thresh)
        
        # Convert back to PIL image for resizing
        img_processed = Image.fromarray(thresh)
        
        # Resize the image to 28x28 pixels, maintaining aspect ratio
        img_processed = ImageOps.pad(img_processed, (28, 28), color='black')
        
        # Normalize the image
        img_array = np.array(img_processed).astype('float32') / 255.0
        img_array = img_array.reshape((1, 28, 28, 1))  # Reshape for the model
        
        # Make a prediction
        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        
        # Return the prediction
        return jsonify({'predicted_digit': int(predicted_digit)})

    return jsonify({'error': 'Invalid file format. Please upload a PNG, JPG, or JPEG file.'})

if __name__ == '__main__':
    app.run(debug=True)
