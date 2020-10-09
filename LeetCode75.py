#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode75.py
# Author: WangYu
# Date  : 2020-10-07

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        one = []
        two = []
        for i in nums:
            if i == 0:
                zero.append(0)
            elif i == 1:
                one.append(1)
            elif i == 2:
                two.append(2)
        zero.extend(one)
        zero.extend(two)
        from copy import deepcopy
        nums = deepcopy(zero)