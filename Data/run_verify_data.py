import pandas as pd
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the file path relative to the script directory
file_path = os.path.join(script_dir, "english.csv")

toggle = True

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
        # Construct the full image path relative to the script directory
        image_path = os.path.join(script_dir, row['image_path'])
        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            toggle = False
    # Display the first few rows of the dataframe
    print(df.head())


print(f"Is All Data Valid: {toggle}")

