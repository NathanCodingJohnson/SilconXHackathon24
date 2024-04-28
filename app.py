from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import easyocr
import time
from model import *

app = Flask(__name__)

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
