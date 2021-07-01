#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode146.py
# Author: WangYu
# Date  : 2021/3/12

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxn = 0
        summ = 0
        y = ['a','e','o','i','u']
        for i in range(k):
            if s[i] in y:
                summ += 1
        maxn = max(summ,maxn)
        for i in range(k,len(s)):
            tmp = s[i]
            if s[i-k] in y:
                summ -= 1
            if s[i] in y:
                summ += 1
                maxn = max(maxn, summ)
        return summ

ss = "tryhard"
s = Solution()
print(s.maxVowels(ss,2))