# Digit Recognition Flask App

## Overview
This project is a Flask-based web application for handwritten digit recognition. It utilizes a neural network model trained on the MNIST dataset to predict digits from user-uploaded images. The application preprocesses images to match the MNIST format (white digits on a black background) before making predictions.

## Installation

### Prerequisites
- Python 3.6+
- pip

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/digit-recognition-flask-app.git
   cd digit-recognition-flask-app
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```sh
   python app.py
   ```

## Usage
After starting the Flask app, navigate to `http://127.0.0.1:5000/` in your web browser. You will be greeted with a simple web interface where you can upload PNG, JPG, or JPEG images of handwritten digits. After uploading an image, the app will display the predicted digit.

### Uploading an Image
1. Click the "Browse..." or "Choose File" button.
2. Select an image file from your computer.
3. Click the "Upload and Predict" button to see the prediction.

## Contributing
Contributions to this project are welcome! Here are a few ways you can help:
- Report bugs and issues.
- Suggest improvements or new features.
- Contribute to the code via pull requests.

Please refer to `CONTRIBUTING.md` for more information on how to contribute.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments
- This project uses the [MNIST dataset](http://yann.lecun.com/exdb/mnist/) for training the digit recognition model.
- Thanks to TensorFlow and Flask for their fantastic libraries.
```
