# -*- coding:utf-8 -*-
from collections import OrderedDict
import datetime
import math
import calendar
import time


def date_format_demo():
    d = datetime.datetime.now()
    print d.strftime("%Y-%m-%d %H:%M")
    print datetime.datetime.strptime('abcd', '%Y-%m-%d')  # exception


def list_demo():
    l = [5, 2, 9, 7, 2, 0]
    l.sort()
    print l
    l.sort(reverse=True)
    print l


def ordered_dict_demo():
    d = {'name': 'Terry', 'gender': 'male', 'age': 20}
    od = OrderedDict()
    for key, value in sorted(d.items(), key=lambda t: t[0]):  # order by key
        od[key] = value
    print od


def time_calculation_demo():
    start = datetime.datetime.strptime('2015-10-01 00:00', '%Y-%m-%d %H:%M')
    end = datetime.datetime.strptime('2015-10-02 23:59', '%Y-%m-%d %H:%M')
    # get seconds of time range
    print int((end - start).total_seconds()) / 60 / 5 + 1


def timestamp_demo():
    d = datetime.datetime.fromtimestamp(1445425800)  # seconds > datetime
    print calendar.timegm(d.timetuple())  # datetime > seconds, no timezone, 1445454600
    print time.mktime(d.timetuple())  # datetime > seconds, with timezone, 1445425800.0


if __name__ == '__main__':
    ordered_dict_demo()
