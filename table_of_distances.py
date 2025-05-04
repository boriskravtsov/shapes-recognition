# May-04-2025
# table_of_distances.py

import numpy as np
from tqdm import tqdm

from max3.src.get_canon_shapes_distance import get_canon_shapes_distance


def table_of_distances(list_filepaths):

    n_shapes = len(list_filepaths)
    n_shapes_x = n_shapes * n_shapes

    D = np.zeros((n_shapes, n_shapes), dtype=np.float32)

    list_indexes = []
    for n in range(n_shapes_x):

        j = n // n_shapes
        i = n % n_shapes

        if i <= j:
            continue

        list_indexes.append((j, i))

    n_calc = len(list_indexes)

    print()
    for n in tqdm(range(n_calc), desc='clustering'):

        temp = list_indexes[n]

        j = temp[0]
        i = temp[1]

        path_j = list_filepaths[j]
        path_i = list_filepaths[i]

        distance = get_canon_shapes_distance(path_i, path_j)

        D[j, i] = distance
        D[i, j] = distance

    return D
