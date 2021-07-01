#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1781.py
# Author: WangYu
# Date  : 2021/3/8
import  collections
class Solution:
    def beautySum(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            for j in range(i+3,len(s)+1):
                tmp = s[i:j]
                if j > len(s):
                    break
                ct = collections.Counter(s[i:j])
                maxn = 0
                minn = 1e9
                for k,v in ct.items():
                    maxn = max(maxn,v)
                    minn = min(minn,v)
                if maxn > minn:
                    cnt += 1
        return cnt
s1 = "aabcb"
s = Solution()
print(s.beautySum(s1))