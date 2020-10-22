#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode567.py
# Author: WangYu
# Date  : 2020-10-19

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        t1 = Counter(s1)
        t2 = Counter(s2[0:len(s1)])
        index = 0
        while index <= len(s2) - len(s1):
            if all(map(lambda x: t1[x] == t2[x], t1.keys())):
                # print(t1)
                # print(t2)
                return True
            if index + len(s1) < len(s2):
                t2[s2[index]] -= 1
                index += 1
                t2[s2[index + len(s1) -1]] += 1
            else:
                break
        return False