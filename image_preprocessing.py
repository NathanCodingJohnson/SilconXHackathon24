import cv2

# Load the image
image = cv2.imread('test_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert grayscale colors
inverted_gray = 255 - gray

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(inverted_gray, (5, 5), 0)

# Apply adaptive thresholding to obtain a binary image
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

# Perform morphological transformations to further clean up the image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
processed_image = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Display the preprocessed image
cv2.imshow('Preprocessed Image', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
