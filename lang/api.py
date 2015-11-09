# -*- coding:utf-8 -*-
import hashlib

def md5_demo():
    print hashlib.md5('abc').hexdigest() # 900150983cd24fb0d6963f7d28e17f72

if __name__ == '__main__':
    md5_demo()