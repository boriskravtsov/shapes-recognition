# Mar-14-2025
# main.py

from pathlib import Path

from cluster_analysis import cluster_analysis
from utils import reset_directory, get_shapes
from table_dist import table_of_distances
from table_dist_progress import table_of_distances_progress
from timer import init_timer, save_elapsed_time_hour_min_sec

init_timer()
reset_directory('RESULTS')

# Getting data for separation
list_filepaths = get_shapes('SHAPES_FOR_SEPARATION_TEST')
# list_filepaths = get_shapes('SHAPES_FOR_SEPARATION_STARS')
# list_filepaths = get_shapes('SHAPES_FOR_SEPARATION_NUMBERS')
# list_filepaths = get_shapes('SHAPES_FOR_SEPARATION_CARDS')

# Calculating distances between shapes, 1 of 2:
# D = table_of_distances(list_filepaths)
D = table_of_distances_progress(list_filepaths)

# Cluster Analysis
final_number_of_clusters = 3
cluster_analysis(
    D,
    final_number_of_clusters,
    list_filepaths)

path_time = Path.cwd() / 'RESULTS' / 'time.txt'
save_elapsed_time_hour_min_sec(path_time)
