#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1566.py
# Author: WangYu
# Date  : 2020-08-31

from typing import List
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)):
            if i + m > len(arr):
                break
            temp1 = arr[i:i + m*k]
            temp2 = arr[i: i + m] * k
            if i + m*k <= len(arr) and temp1 == temp2:
                return True
        return False

s = Solution()
arr = [2,2]
m = 1
k = 2
print(s.containsPattern(arr,m,k))