#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1764.py
# Author: WangYu
# Date  : 2021/2/24

from typing import *
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        cnt = 0
        j = 0
        while i < len(nums):
            if cnt == len(groups):
                return True
            temp = groups[j]
            if nums[i] != temp[0]:
                i+=1
                continue
            elif i+len(temp) > len(nums):
                return False
            elif nums[i] == temp[0]:
                temp2 = nums[i:i+len(temp)]
                if nums[i:i+len(temp)] == temp:
                    i = i+len(temp)
                    j += 1
                    cnt += 1
                else:
                    i+=1
        if cnt == len(groups):
            return True
        else:
            return False

groups = [[1,-1,-1],[3,-2,0]]
nums = [1,-1,0,1,-1,-1,3,-2,0]
s = Solution()
print(s.canChoose(groups,nums))