#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1802.py
# Author: WangYu
# Date  : 2021/3/22

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def find(k):
            summ = 0
            if k > index:
                summ += (k+k-index)*(index+1)/2
            else:
                summ = summ + (index+1-k) + (1+k)*(k)/2

            if k >= (n-index):
                a = (k+k-(n-index)+1)
                b = (n-index)
                summ += a*b/2
            else:
                tmp= (n-index-k)

                summ = summ + (n-index-k) + (1+k)*(k)/2
            summ -= k
            return summ <= maxSum

        l = 1
        r = maxSum
        while l < r:
            mid = (l + r + 1) // 2
            if find(mid):
                l = mid
            else:
                r = mid - 1
        return r

n = 6
index = 1
maxSum = 10
s = Solution()
print(s.maxValue(n,index,maxSum))