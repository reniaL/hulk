import os


def make_parent_dirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

