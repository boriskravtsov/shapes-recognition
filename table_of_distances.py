# Mar-31-2025
# table_of_distances.py

import numpy as np
from tqdm import tqdm

from max3.src.compare_shapes import compare_shapes


def table_of_distances(list_filepaths):

    n_shapes = len(list_filepaths)
    n_shapes_x = n_shapes * n_shapes

    D = np.zeros((n_shapes, n_shapes), dtype=np.float32)

    print()
    for n in tqdm(range(n_shapes_x), desc='clustering'):

        j = n // n_shapes
        i = n % n_shapes

        if i <= j:
            continue

        path_j = list_filepaths[j]
        path_i = list_filepaths[i]

        distance, similarity = compare_shapes(path_i, path_j)

        D[j, i] = distance
        D[i, j] = distance

    return D
