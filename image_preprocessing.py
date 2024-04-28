import cv2
import easyocr

# Load the image using OpenCV
image = cv2.imread('IMG_7566.jpg')

# Perform text recognition using EasyOCR
reader = easyocr.Reader(['en'])  # Specify the languages you want to support
result = reader.readtext(image)

# Extract the text from the result
text = result[0][1]  # Assuming there is only one text detected

print("Detected Text:", text)
