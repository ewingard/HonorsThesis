import os
import random
import shutil

# Set the path to the folder containing the image dataset
dataset_path = "/P/A/T/H/"

# Set the paths for the training and validation folders
train_path = "/PATH/train"
val_path = "/PATH/val"

# Set the split ratio for training and validation (in this case, 80-20)
split_ratio = 0.8

# Get the list of all image files in the dataset folder
all_files = os.listdir(dataset_path)
image_files = [f for f in all_files if f.endswith('.jpg') or f.endswith('.png')]

# Shuffle the list of image files randomly
random.shuffle(image_files)

# Split the image files into training and validation sets
split_index = int(split_ratio * len(image_files))
train_files = image_files[:split_index]
val_files = image_files[split_index:]

# Copy the training files to the training folder
for file_name in train_files:
    src_path = os.path.join(dataset_path, file_name)
    dst_path = os.path.join(train_path, file_name)
    shutil.copy(src_path, dst_path)

# Copy the validation files to the validation folder
for file_name in val_files:
    src_path = os.path.join(dataset_path, file_name)
    dst_path = os.path.join(val_path, file_name)
    shutil.copy(src_path, dst_path)