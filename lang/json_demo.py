# -*- coding:utf-8 -*-
import json


TIMEOUT = 10

def parse():
    content = '[{"name": "Terry", "age": 25}, {"name": "Mary", "age": 20}]'
    l = json.loads(content)
    print len(l)
    print l[0]

if __name__ == '__main__':
    parse()
