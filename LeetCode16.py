#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode16.py
# Author: WangYu
# Date  : 2021/2/25

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 2**31-2
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                summ = nums[i]+nums[l]+nums[r]
                if summ == target:
                    return 0
                elif summ > target:
                    ans = min(abs(summ-target), ans)
                    r -= 1
                else:
                    ans = min(abs(summ-target), ans)
                    l += 1
        return ans

nums = [-1,2,1,-4]
target = 1
s = Solution()
print(s.threeSumClosest(nums,target))