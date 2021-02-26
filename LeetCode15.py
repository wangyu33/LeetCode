#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode15.py
# Author: WangYu
# Date  : 2021/2/25
from typing import List
import bisect
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        if len(nums) <=2:
            return []
        ret = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                tmp = -nums[i]-nums[j]
                id = bisect.bisect_left(nums[j+1:], tmp)
                if j+id+1 < len(nums) and nums[j+id+1] == tmp:
                    ret.add((nums[i],nums[j], tmp))
        return [list(i) for i in ret]

nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))