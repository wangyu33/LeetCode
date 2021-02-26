#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode.py
# Author: WangYu
# Date  : 2021/2/7

from typing import List
class Solution():
    def __init__(self):
        self.minn = 1e9
        self.temp = 1e9+1
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        nums = sorted(nums)
        def dfs(depth,summ):
            if depth == len(nums):
                if self.minn>abs(goal - summ):
                    self.minn = abs(goal - summ)
                    self.temp = summ
                return
            if self.minn == 0:
                return
            if self.minn > abs(goal - summ):
                self.minn = abs(goal - summ)
                self.temp = summ
            if self.temp!= 1e9+1:
                if self.temp > goal and nums[depth] > 0:
                    return
            dfs(depth+1, summ+nums[depth])
            dfs(depth+1, summ)
        dfs(0,0)
        return self.minn
a = [5,-7,3,5]
b = 6
s=Solution()
print(s.minAbsDifference(a,b))