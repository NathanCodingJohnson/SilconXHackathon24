from PIL import Image
import os

def convert_png_to_jpg(png_path, jpg_path):
    try:
        # Open the PNG image
        png_image = Image.open(png_path)

        # Convert the PNG image to RGB mode
        png_image = png_image.convert("RGB")

        # Save the image as JPG
        png_image.save(jpg_path, "JPEG")

        print(f"Converted {png_path} to {jpg_path}")
    except Exception as e:
        print(f"Error converting {png_path}: {str(e)}")

def convert_all_png_to_jpg(directory):
    # Create a new directory to store the converted JPG files
    output_directory = os.path.join(directory, "converted")
    os.makedirs(output_directory, exist_ok=True)

    # Get all PNG files in the directory
    png_files = [f for f in os.listdir(directory) if f.endswith(".png")]

    for png_file in png_files:
        png_path = os.path.join(directory, png_file)
        jpg_file = os.path.splitext(png_file)[0] + ".jpg"
        jpg_path = os.path.join(output_directory, jpg_file)

        # Convert the PNG file to JPG
        convert_png_to_jpg(png_path, jpg_path)

#add a main method
if __name__ == "__main__":
    # Specify the directory containing the PNG files
    directory = "/path/to/png/files"

    # Convert all PNG files to JPG
    convert_all_png_to_jpg(directory)

