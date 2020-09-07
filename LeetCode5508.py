#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5508.py
# Author: WangYu
# Date  : 2020-09-06

from typing import List
from _collections import defaultdict
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sum = 0
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in num1:
            dict1[i*i] = dict1[i*i] + 1
        for i in num2:
            dict2[i*i] = dict2[i*i] + 1
        for i in range(len(num1)-1):
            for j in range(i+1,len(num1)):
                sum += dict2[num1[i]*num1[j]]
        for i in range(len(num2)-1):
            for j in range(i+1,len(num2)):
                sum += dict1[num2[i]*num2[j]]
        return sum

num1, num2 = [1,1],[1,1,1]
s = Solution()
print(s.numTriplets(num1,num2))
