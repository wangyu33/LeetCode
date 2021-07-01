#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1829.py
# Author: WangYu
# Date  : 2021/4/19

from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        target = 2**maximumBit-1
        ret = []
        for i in range(len(nums)):
            if i == 0:
                tmp = nums[i]
            else:
                tmp = tmp^nums[i]
            ret.append(target^tmp)
        return ret[::-1]

s = Solution()
nums = [0,1,1,3]
maximumBit = 2
print(s.getMaximumXor(nums,maximumBit))