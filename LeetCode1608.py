#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1608.py
# Author: WangYu
# Date  : 2020-10-07

from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if nums[0] >= n:
            return n
        for i in range(nums[-1]):
            cnt = 0
            for j in nums:
                if j >= i:
                    cnt += 1
            if cnt == i:
                return cnt
        return -1