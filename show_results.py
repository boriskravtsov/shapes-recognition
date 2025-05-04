# May-04-2025
# show_results.py

from pathlib import Path
import random

from figures.src.fig_scale import fig_basket_scale, fig_canonical_scale
from figures.src.scale_and_caption import basket_scale_and_caption, canonical_scale
from figures.src.create_figure_cluster import create_figure_cluster
from utils.src.dir_support import reset_directory, read_directory_data


def show_results():

    dir_basket_scale = Path.cwd() / '_TEMP' / 'BASKET_SCALE'
    dir_canonical_scale = Path.cwd() / '_TEMP' / 'CANONICAL_SCALE'
    reset_directory(dir_basket_scale)
    reset_directory(dir_canonical_scale)

    dir_clusters = Path.cwd() / 'CLUSTERS'

    """
    Читаем формы из директории BASKET, масштабируем в [166 x 166] для 
    показа в таблице, добавляем заголовки и сохраняем в директории 
    _TEMP/BASKET_SCALE.
    """
    basket_scale_and_caption(dir_basket_scale)

    """
    Читаем формы из директории _CANONICAL, масштабируем в [166 x 166] 
    для показа в таблице и сохраняем в директории _TEMP/_CANONICAL_SCALE.
    """
    canonical_scale(dir_canonical_scale)

    # BASKET_SCALE
    # -------------------------------------------------------------
    list_paths = read_directory_data(dir_basket_scale)
    n_shapes = len(list_paths)
    indexes = list(range(n_shapes))
    random.shuffle(indexes)

    list_paths_random = []
    for n in range(n_shapes):
        index = indexes[n]
        list_paths_random.append(list_paths[index])

    fig_basket_scale(list_paths_random)
    # -------------------------------------------------------------

    # CANONICAL_SCALE
    # -------------------------------------------------------------
    list_paths = read_directory_data(dir_canonical_scale)

    list_paths_random = []
    for n in range(n_shapes):
        index = indexes[n]
        list_paths_random.append(list_paths[index])

    fig_canonical_scale(list_paths_random)
    # -------------------------------------------------------------

    # Визуализация содержимого всех кластеров
    # -------------------------------------------------------------
    folders = [f.name for f in dir_clusters.iterdir() if f.is_dir()]

    for item in folders:
        create_figure_cluster(int(item))
    # -------------------------------------------------------------
