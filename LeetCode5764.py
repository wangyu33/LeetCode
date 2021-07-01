#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5764.py
# Author: WangYu
# Date  : 2021/5/24

from typing import List
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math
        def judge(v):
            t = 0
            for idx,i in enumerate(dist):
                if idx != len(dist)-1:
                    t += math.ceil(i / v)
                else:
                    t += i/v
            return t <= hour

        if len(dist)-1 > hour:
            return -1

        l = 1
        r = 1e9 + 1
        while l < r:
            mid = (l + r) // 2
            if judge(mid):
                r = mid
            else:
                l = mid + 1
        return l

dist = [1,3,2]
hour = 2.7
s = Solution()
print(s.minSpeedOnTime(dist,hour))