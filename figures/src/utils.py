# May-04-2025
# utils.py

import numpy as np

from figures.src import cfg_fig


# Вычисление количества рядов (rows) и столбцов (cols) таблицы
def fig_dimension(n_shapes: int) -> (int, int):

    if n_shapes <= cfg_fig.cols_max:
        rows = 1
        cols = n_shapes
    else:
        cols = cfg_fig.cols_max

        temp1 = n_shapes // cols
        temp2 = n_shapes % cols

        if temp2 == 0:
            rows = temp1
        else:
            rows = temp1 + 1

    return rows, cols


"""
Создание пустого rgb-изображения под будущую таблицу с формами.

Размер изображения fig_empty определяется количеством 
изображений и нашим выбором cfg_fig.cols_max = 8 (максимальным 
числом столбцов в таблице).
"""
def create_empty_rgb(n_shapes):

    rows, cols = fig_dimension(n_shapes)

    fig_base_width = cols * cfg_fig.size_shape_scale + (cols + 1) * cfg_fig.size_space
    fig_base_height = rows * cfg_fig.size_shape_scale + (rows + 1) * cfg_fig.size_space

    fig_empty = np.empty((fig_base_height, fig_base_width, 3), dtype=np.uint8)

    fig_empty.fill(cfg_fig.color_background)

    return fig_empty, rows, cols


"""
Создание пустого grayscale-изображения под будущую таблицу с формами.

Размер изображения fig_empty определяется количеством 
изображений и нашим выбором cfg_fig.cols_max = 8 (максимальным 
числом столбцов в таблице).
"""
def create_empty_grayscale(n_shapes):

    rows, cols = fig_dimension(n_shapes)

    fig_base_width = cols * cfg_fig.size_shape_scale + (cols + 1) * cfg_fig.size_space
    fig_base_height = rows * cfg_fig.size_shape_scale + (rows + 1) * cfg_fig.size_space

    fig_empty = np.empty((fig_base_height, fig_base_width), dtype=np.uint8)

    fig_empty.fill(cfg_fig.color_background)

    return fig_empty, rows, cols
