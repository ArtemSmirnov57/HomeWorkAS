# Lesson 7 dz 1 Smirnov Artem

import os

p_list = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def make_dir(f_list):
    for f, f_s in f_list.items():
        if not os.path.exists(f):
            for i in range(len(f_s)):
                os.makedirs(os.path.join(f, f_s[i]))




make_dir(p_list)