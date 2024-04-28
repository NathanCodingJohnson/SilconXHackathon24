import csv

def read_csv_file(file_path, images, labels):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header if present
        for row in reader:
            image_path, label = row
            images.append(image_path)
            labels.append(label)

file_path = 'Data/english.csv'
file_path_augmented = 'Data/english_augmented.csv'
images = []
features = []
read_csv_file(file_path, images, features)
read_csv_file(file_path, images, features)
print(images)
