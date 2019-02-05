#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1]) as f:
    str = f.read()

print(str.replace("\t", " "), end="")
