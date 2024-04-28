from PIL import Image
import os

script_dir = os.path.dirname(__file__)

def convert_png_to_jpg(png_path, output_directory = script_dir + "\jpeg_output"):
    """
    Converts a PNG image to JPG format and saves it in the specified output directory.

    Args:
        png_path (str): The path of the PNG image file.
        output_directory (str): The directory where the converted JPG image will be saved.

    Returns:
        str: The path of the converted JPG image file.
    """
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Open the PNG image
        png_image = Image.open(png_path)

        # Convert the PNG image to JPG
        jpg_image = png_image.convert("RGB")

        # Create the path for the JPG file
        jpg_file = os.path.splitext(os.path.basename(png_path))[0] + ".jpg"
        jpg_path = os.path.join(output_directory, jpg_file)

        # Save the JPG image
        jpg_image.save(jpg_path)

        print(f"Converted {png_path} to {jpg_path}\n")

        return jpg_path
    except Exception as e:
        print(f"Error converting {png_path}: {str(e)}")
        return None



def crop_and_resize_image(image_path, output_directory = script_dir + "/cropped_resized_output"):
    """
    Crops and resizes an image to a fixed resolution of 50x50 pixels.

    Args:
        image_path (str): The path of the image file to be cropped and resized.
        output_directory (str): The directory where the cropped and resized image will be saved.

    Returns:
        str: The path of the cropped and resized image file.
    """
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Open the image
        image = Image.open(image_path)

        # Crop the image to its minimum size
        image = image.crop(image.getbbox())

        # Resize the image to 50 x 50 resolution
        image = image.resize((50, 50))

        # Create the path for the cropped and resized image
        cropped_resized_file = os.path.splitext(os.path.basename(image_path))[0] + "_c&r.jpg"
        cropped_resized_path = os.path.join(output_directory, cropped_resized_file)

        # Save the cropped and resized image
        image.save(cropped_resized_path, "JPEG")

        print(f"Cropped and resized {image_path} to {cropped_resized_path}\n")

        return cropped_resized_path
    except Exception as e:
        print(f"Error cropping and resizing {image_path}: {str(e)}")



def convert_to_black_and_white(image_path, output_directory = script_dir + "/black_white_output"):
    """
    Converts an image to black and white (grayscale) format and saves it in the specified output directory.

    Args:
        image_path (str): The path of the image file to be converted.
        output_directory (str): The directory where the converted black and white image will be saved.

    Returns:
        None
    """
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Open the image
        image = Image.open(image_path)

        # Convert the image to greyscale
        greyscale_image = image.convert("L")

        # Convert the greyscale image to black and white
        black_white_image = greyscale_image.point(lambda x: 0 if x < 128 else 255, "1")

        # Create the path for the black and white image
        black_white_file = os.path.splitext(os.path.basename(image_path))[0] + "_b&w.jpg"
        black_white_path = os.path.join(output_directory, black_white_file)

        # Save the black and white image
        black_white_image.save(black_white_path, "JPEG")

        print(f"Converted {image_path} to black and white: {black_white_path}\n")
    except Exception as e:
        print(f"Error converting {image_path} to black and white: {str(e)}")

def convert(path):
    """
    Convert a PNG image to a JPG image.

    Args:
        path (str): The path of the PNG image file to be converted.

    Returns:
        None
    """
    script_dir = os.path.dirname(__file__)
    # Convert the PNG image to JPG
    jpg_path = convert_png_to_jpg(path)
    
    if jpg_path is None:
        print(f"Error converting {path} to JPG. Skipping cropping, resizing, and color conversion.")
    else:
        path1 = os.path.join(script_dir, jpg_path)
        crop_and_resize_path = crop_and_resize_image(path1)
        path2 = os.path.join(script_dir, crop_and_resize_path)
        convert_to_black_and_white(path2)

#add a main method
if __name__ == "__main__":
    # Specify the directory containing the PNG files
    # Convert all PNG files to JPG
    #convert_all_png_to_jpg(directory)
    jpeg_file_path = convert_png_to_jpg("testfiles\green-leaf-better-quality.png")
    cropped_path = crop_and_resize_image(jpeg_file_path)
    convert_to_black_and_white(cropped_path)