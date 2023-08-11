# Windows OS: Recursively copy all files from a directory tree to a single directory
import os
import shutil

def copy_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)

        if os.path.isdir(source_item):
            copy_files(source_item, dest_dir)  # Recursively copy files from subdirectories
        elif os.path.isfile(source_item):
            # print("Copying file {} to {}".format(source_item, dest_dir))
            shutil.copy2(source_item, dest_dir)  # Copy individual files

# Example usage:
source_directory = r"C:\Users\xyz\source"  # Replace with your source directory
destination_directory = r"C:\Users\xyz\destination"  # Replace with your destination directory

copy_files(source_directory, destination_directory)
