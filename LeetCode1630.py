#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1630.py
# Author: WangYu
# Date  : 2020/10/26

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            n = nums[l[i]:r[i]+1]
            if len(n) <= 2:
                ans.append(True)
            else:
                n = sorted(n)
                t = n[1] - n[0]
                flag = 1
                for j in range(len(n)-1):
                    if n[j] + t != n[j+1]:
                        flag = 0
                        break
                if flag:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans