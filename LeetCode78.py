#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode78.py
# Author: WangYu
# Date  : 2021/1/29
from typing import List
from copy import deepcopy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = list([])
        ans.append([])
        for i in nums:
            temp = deepcopy(ans)
            for j in temp:
                j.append(i)
                ans.append(j)
        return ans

nums = [1,2,3]
s = Solution()
s.subsets(nums)