#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5717.py
# Author: WangYu
# Date  : 2021/4/19

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                continue
            else:
                cnt += (nums[i-1] - nums[i]+1)
                nums[i] = nums[i-1]+1
                # cnt += (nums[i]-nums[i-1])
        return cnt

s = Solution()
nums = [1,5,2,4,1]
print(s.minOperations(nums))