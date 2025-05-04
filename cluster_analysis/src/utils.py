# May-04-2025
# utils.py

import os
import cv2 as cv


# Extract filenames from filepaths
def get_filenames(list_filepaths):

    list_filenames = []
    for item in list_filepaths:
        file_name = os.path.basename(item)
        list_filenames.append(file_name)

    return list_filenames


def save_shape_in_cluster(dir_data, dir_cluster, shape_filename):

    path_shape_1 = dir_data / shape_filename
    image = cv.imread(path_shape_1, cv.IMREAD_UNCHANGED)

    path_shape_2 = dir_cluster / shape_filename
    cv.imwrite(path_shape_2, image)
