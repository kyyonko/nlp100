#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodules import extract_from_json

lines = extract_from_json("イギリス").split("\n")

for line in lines:
    if "Category" in line:
        print(line)
