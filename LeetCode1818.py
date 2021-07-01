#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1818.py
# Author: WangYu
# Date  : 2021/4/5

from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        kk = 1e9+7
        n1 = sorted(nums1)
        ret = []
        tmp = []
        for i in range(len(nums1)):
            idx = bisect.bisect_left(n1,nums2[i])
            tmp.append(abs(nums1[i]-nums2[i]))
            k = abs(nums1[i]-nums2[i])
            if idx == len(nums1):
                ret.append(k - abs(n1[idx-1] - nums2[i]))
            elif idx-1 >= 0:
                ret.append(k-min(abs(n1[idx]-nums2[i]),abs(n1[idx-1]-nums2[i])))
            else:
                ret.append(k-abs(n1[idx]-nums2[i]))
        maxn = max(ret)
        summ = (sum(tmp)-maxn)%kk
        return int(summ)

nums1 = [56,51,39,1,12,14,58,82,18,41,70,64,18,7,44,90,55,23,11,79,59,76,67,92,60,80,57,11,66,32,76,73,35,65,55,37,38,26,4,7,64,84,98,61,78,1,80,33,5,66,32,30,52,29,41,2,21,83,30,35,21,30,13,26,36,93,81,41,98,23,20,19,45,52,25,51,52,24,2,45,21,97,11,92,28,37,58,29,5,18,98,94,86,65,88,8,75,12,9,66]
nums2 = [64,32,98,65,67,40,71,93,74,24,49,80,98,35,86,52,99,65,15,92,83,84,80,71,46,11,26,70,80,2,81,57,97,12,68,10,49,80,24,18,45,72,33,94,60,5,94,99,14,41,25,83,77,67,49,70,94,83,55,17,61,44,50,62,3,36,67,10,2,39,53,62,44,72,66,7,3,6,80,38,43,100,17,25,24,78,8,4,36,86,9,68,99,64,65,15,42,59,79,66]

s = Solution()
print(s.minAbsoluteSumDiff(nums1,nums2))