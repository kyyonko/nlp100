#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys

f = open(sys.argv[1])
line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)

colnum = int(sys.argv[2]) - 1
 
while line:
    line = line.rstrip("\r\n")
    lines = line.split("\t", -1)
    print(lines[colnum])
    line = f.readline()
f.close

