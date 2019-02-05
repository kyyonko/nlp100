#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from mymodules import extract_from_json

lines = extract_from_json("イギリス").split("\n")

REGEXP = re.compile("^\[\[Category:(.*?)(\|.*)*\]\]$")

for line in lines:
    category_line = re.search(REGEXP, line)
    if category_line is not None:
        print(category_line.group(1))
    
