# Mar-25-2025
# main_figures.py

from pathlib import Path

from figures.src.scale_and_caption import scale_and_caption
from figures.src.create_figure_all_shapes import create_figure_all_shapes
from figures.src.create_figure_cluster import create_figure_cluster
from data_support import reset_directory

dir_figures = Path.cwd() / 'DATA_FIGURES'
dir_figures_all_scale = Path.cwd() / 'DATA_FIGURES' / 'DATA_ALL_SCALE'
dir_figures_results = Path.cwd() / 'DATA_FIGURES' / 'RESULTS'

reset_directory(dir_figures)
reset_directory(dir_figures_all_scale)
reset_directory(dir_figures_results)

# Читаем имена файлов изображений из TEXT/list_filepaths_all.txt
# После масштабирования и добавления подписей к формам получаемые
# модифицированные изображения форм сохраняем в директории
# dir_figures_all_scale.
n_shapes = scale_and_caption(dir_figures_all_scale)

# Создание изображения в виде таблицы со всеми модифицированными
# формами.
create_figure_all_shapes(n_shapes)

# Визуализация содержимого всех кластеров
# -------------------------------------------------------------
dir_clusters = Path.cwd() / 'CLUSTERS'
folders = [f.name for f in dir_clusters.iterdir() if f.is_dir()]

for item in folders:
    create_figure_cluster(int(item))
# -------------------------------------------------------------
