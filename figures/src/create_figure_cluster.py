# May-04-2025
# create_figures_cluster.py

import os
import cv2 as cv
from pathlib import Path

from figures.src import cfg_fig
from figures.src.utils import create_empty_rgb


def create_figure_cluster(cluster_number):

    path_cluster_number = Path.cwd() / 'CLUSTERS' / str(cluster_number)

    n_shapes = len([f for f in os.listdir(path_cluster_number)])
    # print(f"\nNumber of shapes: {n_shapes}")

    fig_empty, rows, cols = create_empty_rgb(n_shapes)

    png_files = list(path_cluster_number.glob("*.png"))

    n = 0
    for shape_path in png_files:

        shape_name = os.path.basename(shape_path)
        shape_path = Path.cwd() / '_TEMP' / 'BASKET_SCALE' / shape_name

        shape_scale = cv.imread(str(shape_path), cv.IMREAD_UNCHANGED)

        nx = n % cols
        ny = n // cols

        shift_x = cfg_fig.size_space + nx * (cfg_fig.size_space + cfg_fig.size_shape_scale)
        shift_y = cfg_fig.size_space + ny * (cfg_fig.size_space + cfg_fig.size_shape_scale)

        fig_empty[
            shift_y:shift_y + cfg_fig.size_shape_scale,
            shift_x:shift_x + cfg_fig.size_shape_scale] = shape_scale

        n += 1

    cluster_n = 'cluster_' + str(cluster_number) + '.png'
    path_cluster_out = Path.cwd() / 'RESULTS' / cluster_n
    cv.imwrite(str(path_cluster_out), fig_empty)
