#!/usr/bin/env python
# coding:utf-8

import sys
from collections import defaultdict

prefectures = defaultdict(int)

with open(sys.argv[1]) as f:
    line = f.readline()
    while line:
        prefectures[line.split()[0]] += 1
        line = f.readline()

for k, v in sorted(prefectures.items(), key = lambda x : x[1], reverse = True):
    print(k)
