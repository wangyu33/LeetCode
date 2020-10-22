#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1300.py
# Author: WangYu
# Date  : 2020-10-20

from typing import List
from functools import lru_cache
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        ans = 0
        l = target//len(arr)
        @lru_cache(None)
        def calc(temp):
            ans1 = 0
            for i in arr:
                if i < temp:
                    ans1 += i
                else:
                    ans1 += temp
            return ans1
        ans = calc(l)
        if ans == target:
            return l
        if sum(arr) <= target:
            return max(arr)
        r = target
        mid = 0
        while l < r:
            mid = (l + r) //2
            if  calc(mid) > target:
                r = mid - 1
            elif calc(mid) == target:
                return mid
            else:
                l = mid + 1
        if abs(calc(l)-target) < abs(calc(mid)-target):
            return l
        elif abs(calc(l)-target) > abs(calc(mid)-target):
            return mid
        else:
            return min(l,mid)

s = Solution()
arr = [60864,25176,27249,21296,20204]
target = 56803

print(s.findBestValue(arr, target))