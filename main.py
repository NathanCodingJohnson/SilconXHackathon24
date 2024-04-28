import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

# Define your CNN model for image feature extraction
def build_cnn_model(input_shape):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(512, activation='relu')
    ])
    return model

# Define your RNN model for text generation
def build_rnn_model(vocab_size):
    model = models.Sequential([
        layers.Embedding(vocab_size, 64),
        layers.LSTM(512, return_sequences=True),
        layers.LSTM(512),
        layers.Dense(vocab_size, activation='softmax')
    ])
    return model

# Load your trained models
cnn_model = build_cnn_model((150, 150, 3)) # Input shape for your images
cnn_model.load_weights('cnn_weights.h5') # Adjust this according to your saved weights file

rnn_model = build_rnn_model(vocab_size) # Vocab size for your text
rnn_model.load_weights('rnn_weights.h5') # Adjust this according to your saved weights file

# Function to generate text from an image
def generate_text_from_image(image_path, cnn_model, rnn_model, tokenizer):
    # Load and preprocess the image
    img = load_img(image_path, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = img_array.reshape((1,) + img_array.shape)
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
    
    # Get features from CNN model
    features = cnn_model.predict(img_array)
    
    # Generate text using RNN model
    start_word = 'startseq'  # Start token
    text = ''
    for i in range(max_length):
        # Tokenize the input sequence
        sequence = tokenizer.texts_to_sequences([start_word])[0]
        sequence = tf.keras.preprocessing.sequence.pad_sequences([sequence], maxlen=max_length)
        
        # Predict next word
        y_pred = rnn_model.predict([features, sequence], verbose=0)
        y_pred = np.argmax(y_pred)
        
        # Convert index to word
        word = word_for_id(y_pred, tokenizer)
        
        # Break if we cannot map the word
        if word is None:
            break
        
        # Append as input for generating the next word
        start_word += ' ' + word
        
        # Break if we predict the end of the sequence
        if word == 'endseq':
            break
    
    return start_word

# Example usage
image_path = 'test_image.jpg'
generated_text = generate_text_from_image(image_path, cnn_model, rnn_model, tokenizer)  # Provide your tokenizer here
print("Generated text:", generated_text)
