import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import random
import csv

import pandas as pd

def read_csv_file(file_path, images, labels):
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        image_path, label = row
        images.append(image_path)
        labels.append(label)


file_path = 'Data/english.csv'
file_path_augmented = 'Data/english_augmented.csv'
images = []
features = []
read_csv_file(file_path, images, features)
read_csv_file(file_path_augmented, images, features)

data = []
for img_path, label in zip(images, features):
    # Load and preprocess the images
    image = tf.keras.preprocessing.image.load_img(img_path, color_mode="grayscale", target_size=(50, 50))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0  # Normalize pixel values to the range [0, 1]
    data.append((image_array, label))

# Shuffle the data
random.shuffle(data)

total_length = len(data)

train_length = int(0.8 * total_length)
test_length = total_length - train_length

# Split the data into training and testing sets
train_data = data[:train_length]
test_data = data[train_length:]

# Prepare training and testing data
x_train, y_train = zip(*train_data)
x_test, y_test = zip(*test_data)

# Convert data to numpy arrays
x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

# Check unique label values
unique_labels = np.unique(y_train)
print('Unique labels:', unique_labels)

# Convert labels to integer indices
label_to_index = {label: index for index, label in enumerate(unique_labels)}
y_train = np.array([label_to_index[label] for label in y_train])
y_test = np.array([label_to_index[label] for label in y_test])

# Reshape the input data for CNN (add channel dimension)
x_train = x_train.reshape(x_train.shape[0], 50, 50, 1)
x_test = x_test.reshape(x_test.shape[0], 50, 50, 1)

# Model Definition
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 50, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(len(unique_labels), activation='softmax')
])

# Model Compilation
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Model Training
model.fit(x_train, y_train, epochs=20, validation_data=(x_test, y_test))

# Model Evaluation
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
