#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode321.py
# Author: WangYu
# Date  : 2021/4/8

from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def find(nums, m):
            stack = []
            n = len(nums)
            for i, num in enumerate(nums):
                while stack and n - i + len(stack) > m and num > stack[-1]:
                    stack.pop()
                stack.append(num)
                if len(stack) > m:
                    stack.pop()
            return stack

        def merge(n1, n2):
            ret = []
            i = 0
            j = 0
            while i < len(n1) and j < len(n2):
                if n1[i:] > n2[j:]:
                    ret.append(n1[i])
                    i += 1
                else:
                    ret.append(n2[j])
                    j += 1
            if i < len(n1):
                ret.extend(n1[i:])
            if j < len(n2):
                ret.extend(n2[j:])
            return ret

        def cp(a, b):
            for i in range(len(a)):
                if a[i] > b[i]:
                    return True
                elif a[i] < b[i]:
                    return False
            return False

        ret = []
        for i in range(k+1):
            j = k - i
            if i <= len(nums1) and j <= len(nums2):
                s1 = find(nums1, i)
                s2 = find(nums2, j)
                s = merge(s1, s2)
                if len(ret) == 0:
                    ret = s
                elif cp(s, ret):
                    ret = s
        return ret

nums1 = [8,1,8,8,6]

nums2 = [4]
s = Solution()
print(s.maxNumber(nums1,nums2,2))