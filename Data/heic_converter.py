"""heic_to_jpeg_converter

This script allows the user to pass in a heic file and save it to a specific directory

This file can also be imported as a module and contains the following
functions:

    * convert_heic_to_jpeg - takes file and saves it to specific output directory
    * main - the main function of the script
"""
import os
from PIL import Image
from pillow_heif import register_heif_opener

def convert_heic_to_jpeg(heic_file, destination_directory):
    """
        Parameters
        ----------
        heic_file : str
            path to heric file
        destination_directory : str
            directory output file will be saved
    """
    try:
        # Register the HEIF opener with Pillow. This step is necessary for Pillow to be able to open HEIC files.
        register_heif_opener()

        # Open the .heic file using Pillow's Image.open function. This function returns an Image object.
        img = Image.open(heic_file)

        # Split the file name and extension using os.path.splitext. This function returns a tuple where the first element is the file name and the second element is the file extension.
        file_name, file_ext = os.path.splitext(os.path.basename(heic_file))

        # Create the name of the output JPEG file by appending ".jpeg" to the file name.
        jpeg_file = file_name + ".jpeg"

        # Join the destination directory with the output file name.
        output_path = os.path.join(destination_directory, jpeg_file)

        # Save the Image object as a JPEG file. The "JPEG" argument specifies the output format.
        img.save(output_path, "JPEG")
        
        # Print a message indicating that the conversion was successful.
        print(f"{heic_file} converted to {output_path}")
    except Exception as e:
        # If an error occurs during the conversion, print an error message. The error message includes the name of the HEIC file and the error that occurred.
        print(f"Error converting {heic_file}: {e}")


if __name__ == "__main__":
    # Specify the path to the .heic file
    heic_file_path = "testfiles/IMG1.heic"
    # Specify the destination directory
    destination_directory = "jpeg_output"
    # Convert the .heic file to .jpeg and save it in the destination directory
    convert_heic_to_jpeg(heic_file_path, destination_directory)
