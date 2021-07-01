#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1854.py
# Author: WangYu
# Date  : 2021/5/10

from typing import List
from collections import defaultdict
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = defaultdict(int)
        for b, death in logs:
            for i in range(b, death):
                d[i] += 1
        maxn = 0
        mdata = -1
        for i in range(1950, 2051):
            if d[i] > maxn:
                mdata = i
                maxn = d[i]
        return mdata

logs = [[1993,1999],[2000,2010]]
s = Solution()
print(s.maximumPopulation(logs))