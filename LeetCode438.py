#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode438.py
# Author: WangYu
# Date  : 2020-10-19

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        t1 = Counter(p)
        t2 = Counter(s[0:len(p)])
        index = 0
        ans = []
        while index <= len(s) - len(p):
            if all(map(lambda x: t1[x] == t2[x], t1.keys())):
                ans.append(index)
            if index + len(p) < len(s):
                t2[s[index]] -= 1
                index += 1
                t2[s[index + len(p) -1]] += 1
            else:
                break
        return ans