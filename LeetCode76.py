#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode76.py
# Author: WangYu
# Date  : 2020-10-19

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t = Counter(t)
        lookup = Counter()
        start = 0
        end = 0
        min_len = float("inf")
        res = ""
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            #print(start, end)
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if end - start < min_len:
                    res = s[start:end]
                    min_len = end - start
                lookup[s[start]] -= 1
                start += 1
        return res

