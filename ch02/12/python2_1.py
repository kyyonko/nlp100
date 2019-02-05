#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys

for line in sys.stdin:
    line = line.rstrip("\r\n")
    line1, line2, line3, line4 = line.split("\t", -1)
    print(line1)
