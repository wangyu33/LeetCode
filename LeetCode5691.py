#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5691.py
# Author: WangYu
# Date  : 2021/3/1

from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 * 6 < l2:
            return -1
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 == sum2:
            return 0
        elif sum1 > sum2:
            tmp = sum1 - sum2
            nums1 = sorted(nums1, reverse = True)
            nums1.extend([1]* (l2-l1+1))
            nums2 = sorted(nums2)
            nums2.append(6)
            id1 = 0
            id2 = 0
            while tmp > 0:
                if nums1[id1] - 1 >= 6 - nums2[id2]:
                    tmp -= nums1[id1] - 1
                    id1 += 1
                else:
                    tmp -= 6 - nums2[id2]
                    id2 += 1
        elif sum1 < sum2:
            tmp = sum2 - sum1
            nums1 = sorted(nums1)
            nums1.extend([6]* (l2-l1+1))
            nums2 = sorted(nums2, reverse = True)
            nums2.append(1)
            id1 = 0
            id2 = 0
            while tmp > 0:
                if nums2[id2] - 1 >= 6 - nums1[id1]:
                    tmp -= nums2[id2] - 1
                    id2 += 1
                else:
                    tmp -= 6 - nums1[id1]
                    id1 += 1
        return id1 + id2

num1 = [1,1,1,1,1,1,1]
num2 = [6]
s= Solution()
print(s.minOperations(num1,num2))


