#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1814.py
# Author: WangYu
# Date  : 2021/4/6

from typing import List
from  functools import lru_cache
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        kk = 1e9 + 7

        @lru_cache(None)
        def rev(a):
            a = str(a)
            return int(a[::-1])

        ret = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]):
                    ret += 1

        return ret