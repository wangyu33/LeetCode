#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode625.py
# Author: WangYu
# Date  : 2020-10-21

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = 0
        t = 0
        n_c = Counter(name)
        t_c = Counter(typed)
        for i in t_c:
            if i not in n_c:
                return False
            if t_c[i] < n_c[i]:
                return False
        while n <len(name) and t < len(typed):
            # print(name[n-1], typed[t])
            if name[n] == typed[t]:
                n += 1
                t += 1
            elif name[n] != typed[t] and typed[t] == name[n-1] and n!= 0:
                t += 1
            elif name[n] != typed[t]:
                return False
        # print(n,t)
        if t == len(typed) and n != len(name):
            return False
        return True