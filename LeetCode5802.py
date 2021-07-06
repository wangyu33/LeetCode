#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5802.py
# Author: WangYu
# Date  : 2021/7/5


class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def ksm(nums, mi, mod):
            ans = 1
            tmp = nums % mod
            while mi:
                if mi & 1:
                    ans = (ans * tmp) % mod
                tmp = (tmp * tmp) % mod
                mi = mi >> 1
            return ans

        MOD = 10 ** 9 + 7
        a = ksm(5, (n + 1) // 2, MOD)
        b = ksm(4, n // 2, MOD)
        return (a * b) % MOD

n = 50
s = Solution()
print(s.countGoodNumbers(n))