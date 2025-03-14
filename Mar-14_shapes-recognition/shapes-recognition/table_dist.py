# Mar-14-2025
# table_dist.py

import numpy as np

from max3.src.set_params import set_params
from max3.src.compare_shapes import compare_shapes


def table_of_distances(list_filepaths):

    set_params(
        13,           # n_peaks (local maxima)
        100,      # canonical_size = 100 x 100 pixels
        0.25)           # cutoff = 0.25, low-pass filter parameter

    print(f'\nWait...')
    n_shapes = len(list_filepaths)
    n_shapes_1 = n_shapes - 1

    D = np.zeros((n_shapes, n_shapes), dtype=np.float32)

    for j in range(n_shapes_1):
        path_j = list_filepaths[j]
        D[j, j] = 0.0

        for i in range(j + 1, n_shapes):
            path_i = list_filepaths[i]

            distance, similarity = compare_shapes(path_i, path_j)

            D[j, i] = distance
            D[i, j] = distance

    return D
