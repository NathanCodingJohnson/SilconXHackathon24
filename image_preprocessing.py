import cv2

# Load the image
image = cv2.imread('test_image2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply bilateral filtering to reduce noise while preserving edges
filtered_image = cv2.bilateralFilter(gray, 1, 75, 75)  # Increase the diameter and sigma values

# Apply Gaussian blur to further reduce noise
blurred = cv2.GaussianBlur(filtered_image, (15, 15), 0)  # Increase the kernel size

# Apply adaptive thresholding to obtain a binary image
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 10)  # Adjust block size and constant

# Perform morphological transformations to further clean up the image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # Adjust the size and shape of the kernel
processed_image = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Invert the colors
inverted_image = cv2.bitwise_not(processed_image)

# Perform additional morphological operations to remove noise and refine text
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
eroded_image = cv2.erode(inverted_image, kernel, iterations=1)
dilated_image = cv2.dilate(eroded_image, kernel, iterations=1)

# Display the preprocessed image with stretchable window
cv2.namedWindow('Preprocessed Image', cv2.WINDOW_NORMAL)
cv2.imshow('Preprocessed Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
