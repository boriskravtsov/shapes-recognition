# Mar-14-2025
# utils.py

import os
import random
from pathlib import Path


# Reset directory
# -------------------------------------------------------------
def reset_directory(dir_name):

    path_dir = Path.cwd() / dir_name

    if path_dir.is_dir():
        for child in path_dir.glob('*'):
            if child.is_file():
                child.unlink()
    else:
        if not path_dir.is_dir():
            path_dir.mkdir()
# -------------------------------------------------------------


# Reading shapes from directory and saving them in a list
# in random order
# -------------------------------------------------------------
def get_shapes(dir_name):

    path_dir = Path.cwd() / dir_name

    list_filepaths = read_data(path_dir)

    random.shuffle(list_filepaths)

    return list_filepaths
# -------------------------------------------------------------


# Reading filepaths of shapes from directory and saving them
# in a list
# -------------------------------------------------------------
def read_data(path_dir):

    list_data = []
    for child in path_dir.glob('*'):
        if child.is_file():

            if child.name.startswith('.'):
                continue

            list_data.append(str(child))

    return list_data
# -------------------------------------------------------------


# Save filepaths for separation in .txt file
# -------------------------------------------------------------
def save_filepaths_for_separation(list_filepaths):

    file_path = Path.cwd() / 'RESULTS' / 'separation_filepaths.txt'

    with open(file_path, 'w') as f:
        for item in list_filepaths:
            f.write(item + '\n')
# -------------------------------------------------------------


# Save filenames for separation in .txt file
# -------------------------------------------------------------
def save_filenames_for_separation(list_filepaths):

    file_path = Path.cwd() / 'RESULTS' / 'separation_filenames.txt'

    with open(file_path, 'w') as f:
        for item in list_filepaths:
            file_name = os.path.basename(item)
            f.write(file_name + '\n')
# -------------------------------------------------------------


# Extract filenames from filepaths
# -------------------------------------------------------------
def get_filenames(list_filepaths):

    list_filenames = []
    for item in list_filepaths:
        file_name = os.path.basename(item)
        list_filenames.append(file_name)

    return list_filenames
# -------------------------------------------------------------


def print_list(any_list):
    for item in any_list:
        print(item)
