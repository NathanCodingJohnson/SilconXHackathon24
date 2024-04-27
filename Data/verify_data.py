import pandas as pd
import os

# Check if the file exists
file_path = "english.csv"
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    # You might want to handle this case gracefully, e.g., exit the script or raise an error
else:
    # Load the dataset
    df = pd.read_csv(file_path)

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
