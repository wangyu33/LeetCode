#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1567.py
# Author: WangYu
# Date  : 2020-08-31

from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)
        start = 0
        ms = []#维护复数数组
        ans = 0
        for index, num in enumerate(nums):
            if num == 0:
                if len(ms) % 2 == 0:
                    ans = max(ans, index - start)
                    start = index + 1
                if len(ms) % 2 == 1:
                    ans = max(ans, index - ms[0] - 1, ms[-1] - start)
                    start = index + 1
                ms = []
            if num < 0:
                ms.append(index)
        return ans

s = Solution()
nums = [1,2,3,5,-6,4,0,10]
print(s.getMaxLen(nums = nums))
