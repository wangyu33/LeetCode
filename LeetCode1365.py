#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1365.py
# Author: WangYu
# Date  : 2020/10/26

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            for j in nums:
                if j < nums[i]:
                    ans[i] += 1
        return ans
