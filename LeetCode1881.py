#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1881.py
# Author: WangYu
# Date  : 2021/5/31

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        ans = int(n+str(x))
        for i in range(len(n)):
            if n[i] == '-':
                continue
            else:
                tmp = n[:i] + str(x) + n[i:]
                tmp = int(tmp)
                ans = max(ans, tmp)
        return str(ans)

ss = "-132"
num = 3
s = Solution()
print(s.maxValue(ss,num))