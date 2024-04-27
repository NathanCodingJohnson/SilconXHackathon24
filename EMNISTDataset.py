import pandas as pd
import urllib.request
import os

# Load the dataset
df = pd.read_csv("https://www.kaggle.com/datasets/dhruvildave/english-handwritten-characters-dataset/data")

# Preprocess the dataframe to get image URLs
df['image_url'] = "https://www.kaggle.com/datasets/dhruvildave/english-handwritten-characters-dataset/data" + df['image']

# Create a directory to save the images
output_dir = "english_handwritten_characters"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to download and save images
def download_and_save_image(url, output_path):
    with urllib.request.urlopen(url) as response:
        with open(output_path, 'wb') as out_file:
            out_file.write(response.read())

# Download and save images
for index, row in df.iterrows():
    image_url = row['image_url']
    image_name = f"{row['image']}"
    output_path = os.path.join(output_dir, image_name)
    download_and_save_image(image_url, output_path)

print("Images downloaded and saved successfully.")
