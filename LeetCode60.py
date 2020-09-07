#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode60.py
# Author: WangYu
# Date  : 2020-09-05

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        from math import factorial
        for i in range(1, n + 1):
            nums.append(i)

        ans = []
        k -= 1

        while len(nums) > 1:
            ids = k // factorial(len(nums) - 1)
            ans.append(nums[ids])
            k -= ids * factorial(len(nums) - 1)
            nums.pop(ids)

        ans += list(nums)

        return ''.join(list(map(str, ans)))

s = Solution()
n,k = 3,2
print(s.getPermutation(n,k))