import os
import pandas as pd
import png_converter as png_converter

# # Read the CSV file into a dataframe
# df = pd.read_csv('Data\english.csv')

# # Iterate over each file in the dataframe
# for file in df['image']:
#     # Convert the file using png_converter
#     png_converter.convert(file)

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the file path relative to the script directory
file_path = os.path.join(script_dir, "english.csv")

df = pd.read_csv(file_path)
df['image_path'] = df['image']

for index, row in df.iterrows():
    image_path = os.path.join(script_dir, row['image_path'])
    png_converter.convert(image_path)