# Mar-17-2025
# data_support.py

import random
from pathlib import Path
import shutil


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
def get_shapes(dir_data):

    list_filepaths = read_data(dir_data)

    list_filepaths_random = list_filepaths.copy()
    random.shuffle(list_filepaths_random)

    # Save list_filepaths_random
    path_file = Path.cwd() / 'RESULTS' / 'list_filepaths_random.txt'
    with open(path_file, 'w+') as file:
        for item in list_filepaths_random:
            file.write('%s\n' % item)

    return list_filepaths_random
# -------------------------------------------------------------


# Saving paths to shapes in a list
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
