# -*- coding:utf-8 -*-
from collections import OrderedDict

def ordered_dict_demo():
    d = OrderedDict()
    d['age'] = 20
    d['name'] = 'Terry'
    for key, value in d.items():
        print key, value

if __name__ == '__main__':
    ordered_dict_demo()