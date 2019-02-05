#!/usr/bin/env python
# coding:utf-8

import sys

f = open(sys.argv[1])
lines = f.readlines()

for line in lines[-int(sys.argv[2]):]:
    print(line, end="")
f.close()
