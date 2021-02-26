#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1208.py
# Author: WangYu
# Date  : 2021/2/5

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        s = list(s)
        t = list(t)
        cha = []
        for i in range(len(s)):
            cha.append(abs(ord(s[i])-ord(t[i])))
        if min(cha) > maxCost:
            return 0
        ret = 0
        maxn = 0
        t = 0
        for i in range(len(s)):
            if i!=0:
                maxn -= cha[i-1]
            while t < len(s) and maxn <= maxCost:
                if maxn + cha[t] > maxCost:
                    break
                else:
                    maxn += cha[t]
                    t = t + 1
            ret = max(ret, t-i)
        return ret

s = Solution()
s1 = "krpgjbjjznpzdfy"
t = "nxargkbydxmsgby"
cost = 14
print(s.equalSubstring(s1,t,cost))
