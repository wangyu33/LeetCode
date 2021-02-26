#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1745.py
# Author: WangYu
# Date  : 2021/2/3

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        d = list(s)
        dp = [i+1 for i in range(len(d))]
        for i in range(len(d)):
            for j in range(i,len(d)):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    if i != 0:
                        dp[j] = min(dp[j],dp[i-1] + 1)
                    else:
                        dp[j] = 1
        print(dp)
        return dp[-1]<=3

t = "gbofdldvwelqiizbievfolrujxnwjmjwsjrjeqecwssgtlteltslfzkblzihcgwjnqaiqbxohcnxulxozzkanaofgoddogfoanakzzoxluxnchoxbqiaqnjwgchizlbkzflstletltgsswceqejrjswjmjwnxjurlofveibziiqlewvdldfobgxebrcrbexv"
s = Solution()
print(s.checkPartitioning(t))