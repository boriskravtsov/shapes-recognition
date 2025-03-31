# Mar-31-2025
# create_figure_all_shapes.py

import os
import cv2 as cv
from pathlib import Path

from figures.src import cfg_fig
from figures.src.utils import create_empty


"""
Заполнение пустого изображения малыми изображениями форм.
"""
def create_figure_all_shapes(n_shapes):

    fig_empty, rows, cols = create_empty(n_shapes)

    path_txt = Path.cwd() / 'TEXT' / 'list_filepaths_all.txt'

    with (open(path_txt, "r") as file):

        n = 0
        for line in file:

            # strip() removes newline characters
            shape_path_text = line.strip()
            shape_name_text = os.path.basename(shape_path_text)

            shape_scale_path = Path.cwd() / '_FIGURES_' / 'DATA_ALL_SCALE' / shape_name_text
            shape_scale = cv.imread(str(shape_scale_path), cv.IMREAD_UNCHANGED)

            nx = n % cols
            ny = n // cols

            shift_x = cfg_fig.size_space + nx * (cfg_fig.size_space + cfg_fig.size_shape_scale)
            shift_y = cfg_fig.size_space + ny * (cfg_fig.size_space + cfg_fig.size_shape_scale)

            fig_empty[
                shift_y:shift_y + cfg_fig.size_shape_scale,
                shift_x:shift_x + cfg_fig.size_shape_scale] = shape_scale

            n += 1

    path_all = Path.cwd() / '_FIGURES_' / 'RESULTS' / 'shapes_all.png'
    cv.imwrite(str(path_all), fig_empty)
