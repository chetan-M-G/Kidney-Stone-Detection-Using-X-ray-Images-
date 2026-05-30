# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400
    
#     # Here we simulate detection logic
#     # In a real application, you would process the image and make predictions
#     result = "Stone Detected"  # Simulated result
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)

import os
from flask import Flask, request, jsonify, render_template
from PIL import Image  # To open and check the image type

app = Flask(__name__)

# Allowed image extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Function to check if the file is an allowed image type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to check if the uploaded image is a valid X-ray image
def is_xray_image(file):
    try:
        img = Image.open(file)
        img.verify()  # Verify the image to check its integrity
        # Here, you could also check the image properties if needed (e.g., size, colors, etc.)
        return True
    except (IOError, SyntaxError) as e:
        return False  # Invalid image or not an X-ray

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the 'file' part is present in the request
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    # If no file is selected
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Check if the file is an allowed image type
    if file and allowed_file(file.filename):
        # Check if the image is a valid X-ray image
        if is_xray_image(file):
            # Simulate detection logic (this is where you would run your actual model)
            result = "Stone Detected"  # Simulated result

            # You can replace this with real detection logic
            return jsonify({'result': result})

        else:
            return jsonify({'error': 'Please upload a valid X-ray image.'}), 400

    else:
        return jsonify({'error': 'Please upload a valid X-ray image (JPG, JPEG, PNG only).'}), 400

if __name__ == '__main__':
    app.run(debug=True)
