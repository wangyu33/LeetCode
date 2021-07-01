#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode42.py
# Author: WangYu
# Date  : 2021/3/16

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        ret = 0
        while l < len(height)-1:
            r = l
            while r < len(height)-1 and height[r+1] < height[l]:
                r += 1
            if r == len(height)-1 and height[r] <= height[l]:
                maxn = max(height[l+1:])
                index = l + height[l+1:].index(maxn) + 1
                for i in range(l+1,index):
                    ret += (maxn-height[i])
                l = index
            elif r== len(height)-1 and height[r] > height[l]:
                index = r
                for i in range(l+1,index+1):
                    ret += (height[l]-height[i])
                l = index + 1
            else:
                index = r
                if r == l:
                    l += 1
                    continue
                for i in range(l+1,index+1):
                    ret += (height[l]-height[i])
                l = index + 1
        return ret

s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))