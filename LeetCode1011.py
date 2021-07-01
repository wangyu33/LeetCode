#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1011.py
# Author: WangYu
# Date  : 2021/4/26


from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def find(t):
            tmp = 0
            summ = 1
            for i in range(len(weights)):
                if tmp + weights[i] <= t:
                    tmp = tmp + weights[i]
                else:
                    tmp = weights[i]
                    summ += 1
                if summ > D:
                    return False
            return True

        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l + r) // 2
            if find(mid):
                r = mid
            else:
                l = mid+1
        return l

weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
s = Solution()
print(s.shipWithinDays(weights,D))