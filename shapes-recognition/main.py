# Mar-17-2025
# main.py

from pathlib import Path

from data_support import reset_directory, get_shapes
from table_of_distances import table_of_distances
from cluster_analysis.src.clustering import clustering
from timer import init_timer, save_elapsed_time_hour_min_sec

init_timer()
reset_directory('RESULTS')

# Getting data for separation
dir_data = Path.cwd() / 'SHAPES_FOR_SEPARATION_TEST'
# dir_data = Path.cwd() / 'SHAPES_FOR_SEPARATION_STARS'
# dir_data = Path.cwd() / 'SHAPES_FOR_SEPARATION_NUMBERS'
# dir_data = Path.cwd() / 'SHAPES_FOR_SEPARATION_CARDS'

list_filepaths_random = get_shapes(dir_data)

# Calculating distances between shapes
# -------------------------------------------------------------
D = table_of_distances(list_filepaths_random)
# -------------------------------------------------------------

# Cluster Analysis
# -------------------------------------------------------------
method = 3
final_number_of_clusters = 3

clustering(
        method,
        final_number_of_clusters,
        dir_data,
        list_filepaths_random,
        D)
# -------------------------------------------------------------

path_time = Path.cwd() / 'RESULTS' / 'time.txt'
save_elapsed_time_hour_min_sec(path_time)
