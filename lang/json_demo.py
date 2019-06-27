# -*- coding:utf-8 -*-
import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def str_to_json():
    content = '[{"name": "Terry", "age": 25}, {"name": "Mary", "age": 20}]'
    jsonobj = json.loads(content)
    print len(jsonobj)
    print jsonobj[1]


def obj_to_json():
    person = Person("Terry", 30)
    jsonobj = json.dumps(person.__dict__)
    print jsonobj


if __name__ == '__main__':
    # str_to_json()
    obj_to_json()
