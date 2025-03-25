# Mar-25-2025
# scale_and_caption.py

import os
import cv2 as cv
from pathlib import Path

from figures.src import cfg_fig


"""
Читаем имена файлов изображений из TEXT/list_filepaths_all.txt.
После масштабирования и добавления названия получаемые изображения
сохраняем в директории dir_figures_all_scale.
"""
def scale_and_caption(dir_figures_all_scale):

    size_scale = (cfg_fig.size_shape_scale, cfg_fig.size_shape_scale)

    font = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    font_color = (0, 0, 0)
    thickness = 1

    # Количество строк в текстовом файле
    path_text_in = Path.cwd() / 'TEXT' / 'list_filepaths_all.txt'
    with open(str(path_text_in), 'r') as file:
        n_shapes = sum(1 for _ in file)

    with (open(path_text_in, "r") as file):

        for line in file:

            # strip() removes newline characters
            path_shape = line.strip()

            shape = cv.imread(str(path_shape), cv.IMREAD_UNCHANGED)

            shape_scale = cv.resize(shape, size_scale, cv.INTER_LANCZOS4)

            shape_name = os.path.basename(path_shape)
            caption = shape_name.removesuffix('.png')

            # подпись под рисунком
            # -------------------------------------------------
            (caption_width, caption_height), baseline = cv.getTextSize(str(caption),
                                                                       font,
                                                                       font_scale,
                                                                       thickness)
            x0 = (cfg_fig.size_shape_scale - caption_width) // 2
            y0 = cfg_fig.size_shape_scale - 5

            cv.putText(shape_scale,
                       caption,
                       (x0, y0),
                       font,
                       font_scale,
                       font_color,
                       thickness,
                       cv.LINE_AA)
            # -------------------------------------------------

            path_out = dir_figures_all_scale / shape_name
            cv.imwrite(str(path_out), shape_scale)

    return n_shapes
