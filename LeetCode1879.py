#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1879.py
# Author: WangYu
# Date  : 2021/5/31

from functools import lru_cache
from typing import List
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, vals):
            if idx == len(nums1) - 1:
                return nums1[idx] ^ vals[0]
            ans = float("inf")
            for val in vals:
                tp = list(vals)
                tp.remove(val)
                ans = min(ans, dfs(idx+1,tuple(tp)) + (nums1[idx] ^ val))
            return ans
        return dfs(0, tuple(sorted(nums2)))


nums1 = [1,0,3]
nums2 = [5,3,4]
s = Solution()
print(s.minimumXORSum(nums1,nums2))
