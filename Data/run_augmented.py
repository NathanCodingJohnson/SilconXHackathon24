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
    image = Image.open(image_path)
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Augment image 11 times
    for i in range(1, 12):
        angle = i * 30
        augmented_image = angled_stretch(image, angle)
        # Append the angle to the filename
        augmented_image_path = os.path.join(output_folder, f"{image_name[:-4]}_{angle}_{i}.png")
        augmented_image.save(augmented_image_path)
        # Write to CSV
        with open("english_augmented.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([augmented_image_path, label])


def main():
    # Get the directory of the script
    script_dir = os.path.dirname(__file__)

    file_path = os.path.join(script_dir, "english.csv")
    # Open english.csv and iterate through each row
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            image_path, label = row
            print(label)
            image_path = os.path.join(script_dir, image_path)  # Adjust the image path
            augment_image(image_path, "augmented", label)

if __name__ == "__main__":
    main()
    print("Done")
