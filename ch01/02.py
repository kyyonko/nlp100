#!/usr/bin/env python
# -*- coding: utf-8 -*-

str1 = "パトカー"
str2 = "タクシー"

print(''.join([char1 + char2 for char1, char2 in zip(str1, str2)]))
