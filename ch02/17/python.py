#!/usr/bin/env python
# coding:utf-8

import sys

prefectures = set()

with open(sys.argv[1]) as f:
    line = f.readline()
    while line:
        prefectures.add(line.split()[0])
        line = f.readline()

prefectures_out = sorted(prefectures)

for pref in prefectures_out:
    print(pref)

