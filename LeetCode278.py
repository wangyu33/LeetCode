#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode278.py
# Author: WangYu
# Date  : 2020-08-28

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid) == True:
                r = mid
            elif isBadVersion(mid) == False:
                l = mid + 1
        return r