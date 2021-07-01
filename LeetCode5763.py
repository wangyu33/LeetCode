#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5763.py
# Author: WangYu
# Date  : 2021/5/24


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxn0 = 0
        maxn1 = 0
        cnt0= 0
        cnt1= 0
        for i in range(len(s)):
            if s[i] == '1' and cnt1==0:
                maxn0 = max(maxn0, cnt0)
                cnt0 = 0
                cnt1+=1
            elif s[i] == '1' and cnt1>0:
                cnt1+=1
            if s[i] == '0' and cnt0==0:
                maxn1 = max(maxn1, cnt1)
                cnt1 = 0
                cnt0 += 1
            elif s[i] == '0' and cnt0>0:
                cnt0+=1
        maxn0 = max(maxn0, cnt0)
        maxn1 = max(maxn1, cnt1)
        print(maxn0,maxn1)
        return maxn1 > maxn0

s = "110100010"
t = Solution()
print(t.checkZeroOnes(s))