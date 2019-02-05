#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

pat = re.compile('[.,]')
print([ len(pat.sub('', word)) for word in str.split() ])
