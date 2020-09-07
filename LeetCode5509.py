#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5509.py
# Author: WangYu
# Date  : 2020-09-06

from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s = list(s)
        ans = 0
        i = 0
        while i < len(s):
            max_cost = 0
            flag = 0
            temp = cost[i]
            while i + 1 < len(s) and s[i + 1] == s[i]:
                flag = 1
                max_cost = max(cost[i + 1], cost[i], max_cost)
                temp += cost[i + 1]
                i = i + 1
            if flag:
                ans = ans + temp - max_cost
            else:
                i = i + 1
        return ans

s,cost = "bbbaaa",[4,9,3,8,8,9]
S= Solution()
print(S.minCost(s,cost))