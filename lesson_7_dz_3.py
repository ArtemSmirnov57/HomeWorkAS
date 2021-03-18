# Lesson 7 dz 3 Smirnov Artem

import os
from shutil import copytree


def copy_dir():
    sourse_dir = 'my_project'
    dir_name = 'templates'

    for root, dirs, files in os.walk(sourse_dir):
        if root.find(dir_name) > 0 and len(files) == 0:
            copytree(os.path.join(root), dir_name, dirs_exist_ok=True)


if __name__ == '__main__':
    copy_dir()





