#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode844.py
# Author: WangYu
# Date  : 2020-10-19

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a = []
        b = []
        for i in S:
            if i != '#':
                a.append(i)
            elif i == '#'and a != []:
                a.pop(-1)
        for i in T:
            if i != '#':
                b.append(i)
            elif i == '#'and b != []:
                b.pop(-1)
        return ''.join(a) == ''.join(b)