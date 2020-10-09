#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1610.py
# Author: WangYu
# Date  : 2020-10-07

import math
from typing import List
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        anl = []
        ans = 0
        for i in points:
            if i == location:
                ans += 1
            else:
                anl_temp = math.degrees(math.atan2(i[1] - location[1], i[0] - location[0]))
                anl.append(anl_temp)
        maxn = 0
        anl = sorted(anl)
        anl.extend(list(map(lambda x: x + 360, anl)))
        res, i, j, n = 0, 0, 0, len(anl)
        while j < n:
            while anl[j] - anl[i] > angle:
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res + ans

p = [[956,232],[438,752],[595,297],[508,143],[111,594],[645,824],[758,434],[447,423],[825,356],[807,377]]
angle = 38
po = [74,581]
s = Solution()
print(s.visiblePoints(p,angle,po))