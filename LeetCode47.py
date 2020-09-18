#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode47.py
# Author: WangYu
# Date  : 2020-09-18

from typing import List
from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        flag = [0] * len(nums)
        D = defaultdict(int)
        ans = []

        def dfs(temp):
            if D[tuple(temp)] == 1:
                return
            if len(temp) == len(nums):
                ans.append(temp[:])
                return
            for i in range(len(nums)):
                if flag[i] == 0:
                    flag[i] = 1
                    dfs(temp + [nums[i]])
                    D[tuple(temp + [nums[i]])] = 1
                    flag[i] = 0
        for i in range(len(nums)):
            flag[i] = 1
            dfs([nums[i]])
            flag[i] = 0
        # ans = set([tuple(i) for i in ans])
        # ans = [list(i) for i in ans]
        return ans

s = Solution()
a = [1,1,2]
print(s.permuteUnique(a))