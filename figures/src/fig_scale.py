# May-04-2025
# fig_scale.py

import cv2 as cv
from pathlib import Path

from figures.src import cfg_fig
from figures.src.utils import create_empty_rgb, create_empty_grayscale


def fig_basket_scale(list_data):

    n_shapes = len(list_data)

    fig_empty, rows, cols = create_empty_rgb(n_shapes)

    n = 0
    for path in list_data:

        shape_scale = cv.imread(str(path), cv.IMREAD_UNCHANGED)

        nx = n % cols
        ny = n // cols

        shift_x = cfg_fig.size_space + nx * (cfg_fig.size_space + cfg_fig.size_shape_scale)
        shift_y = cfg_fig.size_space + ny * (cfg_fig.size_space + cfg_fig.size_shape_scale)

        fig_empty[
            shift_y:shift_y + cfg_fig.size_shape_scale,
            shift_x:shift_x + cfg_fig.size_shape_scale] = shape_scale

        n += 1

    path_fig = Path.cwd() / 'RESULTS' / 'basket_shapes.png'
    cv.imwrite(str(path_fig), fig_empty)


def fig_canonical_scale(list_data):

    n_shapes = len(list_data)

    fig_empty, rows, cols = create_empty_grayscale(n_shapes)

    n = 0
    for path in list_data:

        shape_scale = cv.imread(str(path), cv.IMREAD_UNCHANGED)

        nx = n % cols
        ny = n // cols

        shift_x = cfg_fig.size_space + nx * (cfg_fig.size_space + cfg_fig.size_shape_scale)
        shift_y = cfg_fig.size_space + ny * (cfg_fig.size_space + cfg_fig.size_shape_scale)

        fig_empty[
            shift_y:shift_y + cfg_fig.size_shape_scale,
            shift_x:shift_x + cfg_fig.size_shape_scale] = shape_scale

        n += 1

    path_fig = Path.cwd() / 'RESULTS' / 'basket_shapes_canonical.png'
    cv.imwrite(str(path_fig), fig_empty)
