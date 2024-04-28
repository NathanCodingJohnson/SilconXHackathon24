import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import logging
import re

image = cv2.imread('test4.jpg')
# Load the Keras model from the .h5 file
model = load_model('EnglishCharacterClassifierModel.keras')

# Function to preprocess an image
def preprocess_image(image):
    #grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    input_shape = model.input_shape[1:3]
    resized_image = cv2.resize(gray_image, input_shape)
    input_data = np.expand_dims(resized_image, axis=0)
    input_data = input_data.astype('float32') / 255.0
    
    return input_data

import easyocr
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
logging.getLogger('easyocr').setLevel(logging.ERROR) 
def predict_characters(image):
    # Preprocess the image
    input_data = preprocess_image(image)
    predictions = model.predict(input_data)
    
    characters = [chr(np.argmax(prediction) + ord('A')) for prediction in predictions]
    
    return characters

"""
def predict_characters(image):
    # Preprocess the image
    input_data = preprocess_image(image)
    predictions = model.predict(input_data)
    
    characters = [chr(np.argmax(prediction) + ord('A')) for prediction in predictions]
    
    return characters
reader = easyocr.Reader(['en'])
"""


# Function to detect words from a list of characters
def detect_words(characters, space_threshold=5):
    words = []
    current_word = ""
    for char in characters:
        if char != " ":  # If character is not a space, add it to the current word
            current_word += char
        else:  
            if current_word:  
                words.append(current_word)
                current_word = ""  
            # elif len(current_word) == 0 and len(words) > 0 and len(words[-1]) >= space_threshold:
            elif len(current_word) == 0 and len(words) > 0 and len(words[-1]) >= space_threshold:
                words.append(" ")
    # Add the last word if it exists
    if current_word:
        words.append(current_word)
    return words

# Load the input image

# Predict characters from the image
#characters = predict_characters(image)

# Detect words from the predicted characters
#words = detect_words(characters)

# Print the detected words
#print("Detected Words:", words)
reader = easyocr.Reader(['en'])
def process_image(image_file):
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    result = reader.readtext(image)
    detected_text = result[0][1] if result else "No text detected"
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', detected_text)
    return cleaned_text

def remove_noise(image):
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

def convert_to_grayscale(image):
    """Converts an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_image(image, width=None, height=None, interpolation=cv2.INTER_AREA):
    """Resizes an image to the specified width and height."""
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=interpolation)
    return resized

def threshold_image(image, threshold_value=127, max_value=255, threshold_type=cv2.THRESH_BINARY):
    """Applies a threshold to the image."""
    _, thresholded = cv2.threshold(image, threshold_value, max_value, threshold_type)
    return thresholded