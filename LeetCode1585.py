#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1585.py
# Author: WangYu
# Date  : 2020-09-14
from collections import *
import collections
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if Counter(s) != Counter(t):
            return False

        n = len(s)
        pos = {i: collections.deque() for i in range(10)}
        for i, digit in enumerate(s):
            pos[int(digit)].append(i)

        for i, digit in enumerate(t):
            d = int(digit)
            if not pos[d]:
                return False
            if any(pos[j] and pos[j][0] < pos[d][0] for j in range(d)):
                return False
            pos[d].popleft()

        return True

S= Solution()
s = "34521"
t = "23415"
print(S.isTransformable(s,t))