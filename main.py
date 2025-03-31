# Mar-31-2025
# main.py

from pathlib import Path

from data_support import reset_directory, get_shapes
from table_of_distances import table_of_distances
from cluster_analysis.src.clustering import clustering
from timer import init_timer, save_elapsed_time_hour_min_sec


# DATA
# -------------------------------------------------------------
dir_known = Path.cwd() / 'DATA_KNOWN'
dir_unknown = Path.cwd() / 'DATA_UNKNOWN'
dir_all = Path.cwd() / 'DATA_ALL'
# -------------------------------------------------------------

init_timer()
reset_directory('CLUSTERS')
reset_directory('TEXT')
reset_directory('DATA_ALL')


list_filepaths_all = get_shapes(dir_known, dir_unknown, dir_all)

# Calculating distances between shapes
# -------------------------------------------------------------
D = table_of_distances(list_filepaths_all)
# -------------------------------------------------------------

# Cluster Analysis
# -------------------------------------------------------------
method = 3
known_classes = 8
unknown_classes = 0
final_number_of_clusters = known_classes + unknown_classes

clustering(
        method,
        final_number_of_clusters,
        dir_all,
        list_filepaths_all,
        D)
# -------------------------------------------------------------

path_time = Path.cwd() / 'TEXT' / 'time.txt'
save_elapsed_time_hour_min_sec(path_time)
