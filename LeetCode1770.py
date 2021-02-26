#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1770.py
# Author: WangYu
# Date  : 2021/2/23

from typing import List
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        maxn = 0
        L = [(nums, multipliers,0)]
        while len(L) > 0:
            a,b,summ = L[0]
            L.pop(0)
            if len(b) == 0:
                maxn = max(maxn, summ)
                continue
            sum1 = summ + a[0] * b[0]
            sum2 = summ + a[-1]*b[0]
            L.append((a[1:],b[1:],sum1))
            L.append((a[:-1],b[1:],sum2))
        return maxn

nums = [1,2,3]
multipliers = [3,2,1]
s = Solution()
print(s.maximumScore(nums,multipliers))