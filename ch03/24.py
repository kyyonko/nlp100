#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from mymodules import extract_from_json

lines = extract_from_json("イギリス").split("\n")

REGEXP = re.compile(u"(File|ファイル):(.*?)\|")

for line in lines:
    section_line = re.search(REGEXP, line)
    if section_line is not None:
        print(section_line.group(2))
