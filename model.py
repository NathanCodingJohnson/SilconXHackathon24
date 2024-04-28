import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

import random

import csv

def read_csv_file(file_path, images, labels):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header if present
        for row in reader:
            image_path, label = row
            images.append(image_path)
            labels.append(label)

file_path = 'Data/english.csv'
#file_path_augmented = 'Data/english_augmented.csv'
images = []
features = []
read_csv_file(file_path, images, features)
img_arrs = []

for img in images:
# Load and preprocess the images
    image = tf.keras.preprocessing.image.load_img(img, color_mode="grayscale", target_size=(50, 50))
    image_array = tf.keras.preprocessing.image.img_to_array(img)
    image_array = image_array / 255.0  # Normalize pixel values to the range [0, 1]
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    img_arrs.append(image_array)

data = ((img_arrs, features))


#read_csv_file(file_path_augmented, images, features)
random.shuffle(data)

total_length = len(data)

train_length = int(0.8 * total_length)
test_length = total_length - train_length

# Split the data into training and testing sets
train_data = data[:train_length]
test_data = data[train_length:]



# Step 2: Model Definition
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Step 3: Model Compilation
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Step 4: Model Training
# Assuming you have a dataset with features and labels
x_train, y_train = zip(*train_data)
x_test, y_test = zip(*test_data)

model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Step 5: Model Evaluation
test_loss, test_acc = model.evaluate(x_test, y_test)

print('Test accuracy:', test_acc)
