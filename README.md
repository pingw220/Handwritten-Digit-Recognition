# Handwritten Digit Recognition Project

## Overview
This project is a Flask-based web application for handwritten digit recognition. It utilizes a neural network model trained on the MNIST dataset to predict digits from user-uploaded images. The application preprocesses images to match the MNIST format (white digits on a black background) before making predictions.

## Introduction
This Handwritten Digit Recognition Project is a lightweight web application that demonstrates practical machine learning by recognizing handwritten digits from user-uploaded images. Built with Flask, a Python web framework, and leveraging a neural network model trained on the famous MNIST dataset, this application showcases the intersection of web development and artificial intelligence.

The project simplifies the process of digit recognition into an intuitive web interface. Users can upload images in PNG, JPG, or JPEG formats, and the backend, powered by TensorFlow and PIL (Python Imaging Library), preprocesses these images to fit the model's expectations. This preprocessing includes converting images to grayscale, resizing to 28x28 pixels, inverting colors if necessary to match the MNIST training data format, and normalizing pixel values.

Once an image is uploaded, the application applies these preprocessing steps and feeds the image to the pre-trained model, which then predicts the digit. The predicted digit is immediately returned to the user, demonstrating an effective blend of web technology and machine learning for a simple yet powerful application.

Designed to be both a learning tool and a base for further development, this project exemplifies how machine learning models can be integrated into real-world applications, providing insights into the model's behavior and interactions with different types of input data.

## Installation
### Setup
To run this project locally or explore its capabilities, follow these steps:
1. **Clone the Repository**: Clone this project to your local machine to get started.
2. **Set Up Your Environment**: Ensure you have Python installed and create a virtual environment.
3. **Download the Model**: Access the pre-trained model from [[Cloud Storage URL](https://drive.google.com/file/d/1lWPMxS1VKzsvhowwRo7kBC1aqzt3OqXu/view?usp=sharing)] and place it in the designated directory within the project.
4. **Launch the Web App**: Run the Streamlit app using `python app.py` and navigate to the provided local URL to start classifying tennis court images.

## Usage
After starting the Flask app, navigate to `http://127.0.0.1:5000/` in your web browser. You will be greeted with a simple web interface where you can upload PNG, JPG, or JPEG images of handwritten digits. After uploading an image, the app will display the predicted digit.

### Uploading an Image
1. Click the "Browse..." or "Choose File" button.
2. Select an image file from your computer.
3. Click the "Upload and Predict" button to see the prediction.

## Acknowledgments
- This project uses the [MNIST dataset](http://yann.lecun.com/exdb/mnist/) for training the digit recognition model.
- Thanks to TensorFlow and Flask for their fantastic libraries.
```
