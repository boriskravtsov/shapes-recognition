# May-04-2025
# clustering.py

import numpy as np
from pathlib import Path

from cluster_analysis.src.utils import get_filenames, save_shape_in_cluster


def clustering(
        final_number_of_clusters,
        clustering_method,
        dir_data,
        list_filepaths,
        D):

    # ---------------------------------------------------------
    list_filenames = get_filenames(list_filepaths)

    n_shapes = len(list_filenames)
    n_shapes_1 = n_shapes - 1

    clusters = [['' for i in range(n_shapes)] for j in range(n_shapes)]

    m = 0
    for n in range(n_shapes):
        filename = list_filenames[n]
        clusters[n][m] = filename
        m += 1

    """
    print(f'\nНачальное содержимое каждого кластера:')
    for n in range(n_shapes):
        print(f'cluster {n}:\t {clusters[n]}')
    print()
    """
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    M = np.zeros(n_shapes, dtype=np.int32)
    N = np.zeros(n_shapes, dtype=np.int32)

    # M - number of objects in the cluster
    # N - object numbers in the cluster
    for m in range(n_shapes):
        M[m] = 1
        N[m] = m
    # ---------------------------------------------------------

    # Слияние всех объектов в один кластер размером n_shapes
    # ---------------------------------------------------------
    for _ in range(n_shapes_1):     # n_shapes_1 - число слияний

        # Определение минимального расстояния в таблице
        # -----------------------------------------------------
        minDist = np.finfo(float).max      # max_float
        k = -1
        l = -1

        for j in range(n_shapes_1):
            if M[j] == 0:
                continue

            for i in range(j+1, n_shapes):
                if M[i] == 0:
                    continue

                if D[j, i] < minDist:
                    minDist = D[j, i]
                    k = j
                    l = i
        # -----------------------------------------------------

        # Пересчет после слияния.
        # -----------------------------------------------------
        for j in range(n_shapes):
            if M[j] == 0:
                continue

            match clustering_method:

                case 1:     # "Min Distance"
                    D[k, j] = (D[j, k] + D[j, l] - abs(D[j, k] - D[j, l])) * 0.5
                    D[j, k] = D[k, j]

                case 2:     # "Max Distance"
                    D[k, j] = (D[j, k] + D[j, l] + abs(D[j, k] - D[j, l])) * 0.5
                    D[j, k] = D[k, j]

                case 3:     # Method of Ward
                    D[k, j] = ((M[j] + M[k]) * D[j, k] + (M[j] + M[l]) * D[j, l] -
                                M[j] * minDist) / (M[j] + M[k] + M[l])
                    D[j, k] = D[k, j]

        for j in range(n_shapes):
            D[l, j] = 0.0
            D[j, l] = 0.0
        # -----------------------------------------------------

        # -----------------------------------------------------
        M[k] += M[l]    # M[] - количество объектов в кластере.
        M[l] = 0

        for n in range(n_shapes):
            if clusters[l][n] != '':
                clusters[k][n] = clusters[l][n]

        for n in range(n_shapes):
            clusters[l][n] = ''

        for m in range(n_shapes):
            if N[m] == l:
                N[m] = -1   # N[] - номера объектов в кластере.
        # -----------------------------------------------------

        # Вывод промежуточных результатов.
        # -----------------------------------------------------
        """
        print(f'\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

        print(f'Слияние кластеров:\t\t K = {k}\t\t L = {l}\t\t minDist = {minDist: .3f}')

        print(f'\nKоличество объектов в каждом из кластеров:')
        print(f'\t {M}')

        print(f'\nНомера объектов в каждом кластере:')
        print(f'\t {N}')

        print(f'\nСодержимое каждого кластера:')
        for n in range(n_shapes):
            if M[n] > 0:
                print(f'cluster {n}:')
                for item in clusters[n]:
                    if item != '':
                        print(f'\t{item}')
        print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        """
        # -----------------------------------------------------

        n_clusters = 0
        for m in range(n_shapes):
            if M[m] == 0:
                continue
            n_clusters += 1

        if n_clusters == final_number_of_clusters:
            # print(f'\nFinal content of clusters:')
            for n in range(n_shapes):
                if M[n] > 0:
                    # print(f'cluster #{n}:')
                    for item in clusters[n]:
                        if item != '':
                            # print(f'\t {item}')

                            dir_cluster = Path.cwd() / 'CLUSTERS' / str(n)
                            if not dir_cluster.exists():
                                dir_cluster.mkdir()
                            save_shape_in_cluster(dir_data, dir_cluster, item)
            break
