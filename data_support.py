# Mar-25-2025
# data_support.py

import os
import shutil
import random
from pathlib import Path


# Reset directory
# -------------------------------------------------------------
def reset_directory(dir_name):

    path_dir = Path.cwd() / dir_name

    if path_dir.is_dir():
        for item in path_dir.iterdir():
            if item.is_file():
                item.unlink()           # Remove file
            elif item.is_dir():
                shutil.rmtree(item)     # Remove directory
    else:
        path_dir.mkdir()
# -------------------------------------------------------------


# Saving paths to shapes in the list in random order
# -------------------------------------------------------------
def get_shapes(dir_known, dir_unknown, dir_all):

    # Copy shapes from dir_known to dir_all
    for file_name in os.listdir(dir_known):
        full_file_name = os.path.join(dir_known, file_name)
        if os.path.isfile(full_file_name):  # Check if it's a file
            shutil.copy2(full_file_name, dir_all)

    # Copy shapes from dir_unknown to dir_all
    for file_name in os.listdir(dir_unknown):
        full_file_name = os.path.join(dir_unknown, file_name)
        if os.path.isfile(full_file_name):  # Check if it's a file
            shutil.copy2(full_file_name, dir_all)

    # Shuffle the list items
    list_filepaths_all = read_data(dir_all)
    random.shuffle(list_filepaths_all)

    # Save list_filepaths_all
    path_file = Path.cwd() / 'TEXT' / 'list_filepaths_all.txt'
    with open(path_file, 'w+') as file:
        for item in list_filepaths_all:
            file.write('%s\n' % item)

    return list_filepaths_all
# -------------------------------------------------------------


# Saving paths to shapes in the list
# -------------------------------------------------------------
def read_data(dir_data):

    list_data = []
    for child in dir_data.glob('*'):
        if child.is_file():

            if child.name.startswith('.'):
                continue

            list_data.append(str(child))

    return list_data
# -------------------------------------------------------------


# Print list
# -------------------------------------------------------------
def print_list(list_data):
    n = 0
    for item in list_data:
        print(f'{n}\t {item}')
        n += 1
# -------------------------------------------------------------
