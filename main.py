# May-04-2025
# main.py

from pathlib import Path

from max3 import to_canonical_1
from table_of_distances import table_of_distances
from cluster_analysis.src.clustering import clustering
from utils.src.dir_support import (
    reset_directory, remove_directory, read_directory_data)
from show_results import show_results
from utils.src.timer import init_timer, save_elapsed_time_hour_min_sec


"""
Important: Images in the BASKET require PNG format and the RGB color space.
"""
dir_basket = Path.cwd() / 'BASKET'
list_basket_paths = read_directory_data(dir_basket)
n_basket_shapes = len(list_basket_paths)

print(f'\nThere are {n_basket_shapes} shapes in the BASKET folder ready for clustering.')
input_string = input('Please enter the desired number of clusters: ')
final_number_of_clusters = int(input_string)

reset_directory('RESULTS')
reset_directory('CLUSTERS')
reset_directory('_CANONICAL')
reset_directory('_TEMP')

# Изображения из директории BASKET преобразуем в канонический вид -
# grayscale, [100 x 100] pixels и помещаем в директорию _CANONICAL.
dir_canonical = Path.cwd() / '_CANONICAL'
to_canonical_1(dir_canonical, list_basket_paths)
list_canonical_filepaths = read_directory_data(dir_canonical)

init_timer()

# Calculating mutual distances between shapes
D = table_of_distances(list_canonical_filepaths)

# Cluster Analysis
clustering_method = 3
clustering(
        final_number_of_clusters,
        clustering_method,
        dir_basket,
        list_canonical_filepaths,
        D)

show_results()

path_time = Path.cwd() / 'RESULTS' / 'time.txt'
save_elapsed_time_hour_min_sec(path_time)

# Clean up
remove_directory('_CANONICAL')
remove_directory('_TEMP')
