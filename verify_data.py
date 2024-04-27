import pandas as pd
import os

# Load the dataset
df = pd.read_csv("english.csv")

# Preprocess the dataframe
df['image_path'] = df['image']

# Verify if image files exist
for index, row in df.iterrows():
    image_path = row['image_path']
    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
print("Data All Valid")
# Display the first few rows of the dataframe
print(df.head())
