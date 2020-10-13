#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode120.py
# Author: WangYu
# Date  : 2020-10-09

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * len(triangle[-1])
        dp[0] = triangle[0][0]
        for temp in triangle[1:]:
            dp1 = copy.deepcopy(dp)
            # print(dp)
            for index, num in enumerate(temp):
                if index == 0:
                    dp1[index] = dp[index] + num
                elif index == len(temp) - 1:
                    dp1[index] = dp[index - 1] + num
                else:
                    dp1[index] = min(dp[index], dp[index - 1]) + num
            dp = dp1
        return min(dp)

