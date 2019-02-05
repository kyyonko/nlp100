#!/usr/bin/env python
# coding:utf-8

import sys, math
assert len(sys.argv) == 3, "[usage]: python 16.ファイルをN分割する.py [N]"

text = [line for line in open(sys.argv[1])]
unit = math.ceil( len(text) / int(sys.argv[2]) )

for i in range( (int(sys.argv[2])) ):
    with open("file" + str(i + 1) + ".txt", "w") as f:
        f.write("".join(text[i*unit:(i+1)*unit]))
