import csv
import os
from PIL import Image


def angled_stretch(image, angle):
    # Create a white background image of the same size
    bg = Image.new('RGB', image.size, color=(255, 255, 255))
    # Convert the image to RGBA mode
    image_rgba = image.convert('RGBA')
    # Paste the original image onto the white background
    bg.paste(image_rgba, (0, 0), image_rgba)
    # Rotate the combined image
    rotated_image = bg.rotate(angle, resample=Image.BICUBIC, expand=True, fillcolor=(255, 255, 255))
    return rotated_image


def augment_image(image_path, output_folder, label):
    image_name = os.path.basename(image_path)
    image_name_without_extension, extension = os.path.splitext(image_name)
    image = Image.open(image_path)
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Augment image 11 times
    for i in range(1, 12):
        angle = i * 30
        augmented_image = angled_stretch(image, angle)
        # Save augmented image with degree of rotation appended to filename
        augmented_image_name = f"{image_name_without_extension}-{angle}{extension}"
        augmented_image_path = os.path.join(output_folder, augmented_image_name)
        augmented_image.save(augmented_image_path)
        # Write to CSV with complete path including directory
        augmented_image_csv_name = f"Augmented_Img/{augmented_image_name}"  # Path in CSV
        with open("Data/english_augmented.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write image and label in the first row
            if csvfile.tell() == 0:
                writer.writerow(["image", "label"])
            writer.writerow([augmented_image_csv_name, label])


def clear_folder(folder_path):
    # Clear the contents of the folder
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                clear_folder(file_path)
        os.rmdir(folder_path)


def clear_csv(file_path):
    # Clear the contents of the CSV file
    if os.path.exists(file_path):
        os.remove(file_path)


def main():
    # Get the directory of the script
    script_dir = os.path.dirname(__file__)
    
    file_path = os.path.join(script_dir, "english.csv")

    augmented_folder = os.path.join(script_dir, "Augmented_Img")

    clear_folder(augmented_folder)  # Clear Augmented folder on run
    clear_csv(os.path.join(script_dir, "Data", "english_augmented.csv"))  # Clear the augmented CSV file

    # Open english.csv and iterate through each row
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            image_path, label = row
            print(label)
            image_path = os.path.join(script_dir, image_path)  # Adjust the image path
            augment_image(image_path, augmented_folder, label)

    print("Done")


if __name__ == "__main__":
    main()
