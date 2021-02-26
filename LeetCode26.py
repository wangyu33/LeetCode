#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode26.py
# Author: WangYu
# Date  : 2021/2/25

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                r += 1
            else:
                while r < len(nums) and nums[l] == nums[r]:
                    r += 1
                if r >= len(nums):
                    return l
                l += 1
                nums[l] = nums[r]
        return l

nums = [1,1,2]
s = Solution()
print(s.removeDuplicates(nums))