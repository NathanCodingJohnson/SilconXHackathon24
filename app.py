from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import easyocr
import time

app = Flask(__name__)
reader = easyocr.Reader(['en'])

def process_image(image_file):
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    result = reader.readtext(image)
    detected_text = result[0][1] if result else "No text detected"
    return detected_text

def debounce(func, wait):
    last_call = 0
    def debounced_function(*args, **kwargs):
        nonlocal last_call
        now = time.time()
        if now - last_call < wait:
            return 
        last_call = now
        return func(*args, **kwargs)
    return debounced_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    try:
        detected_text = process_image(image_file)
        return jsonify({'text': detected_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
