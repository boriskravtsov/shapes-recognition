# Mar-14-2025
# table_dist_progress.py

import numpy as np
from tqdm import tqdm

from max3.src.set_params import set_params
from max3.src.compare_shapes import compare_shapes


def table_of_distances_progress(list_filepaths):

    set_params(
        13,           # n_peaks (local maxima)
        100,      # canonical_size = 100 x 100 pixels
        0.25)           # cutoff = 0.25, low-pass filter parameter

    print()
    n_shapes = len(list_filepaths)
    n_shapes_1 = n_shapes - 1

    D = np.zeros((n_shapes, n_shapes), dtype=np.float32)

    for j in tqdm(range(n_shapes_1), desc='separation'):
        path_j = list_filepaths[j]
        D[j, j] = 0.0

        for i in range(j + 1, n_shapes):
            path_i = list_filepaths[i]

            distance, similarity = compare_shapes(path_i, path_j)

            D[j, i] = distance
            D[i, j] = distance

    return D
