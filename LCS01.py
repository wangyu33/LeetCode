#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LCS01.py
# Author: WangYu
# Date  : 2021/6/21

import bisect
class Solution:
    def leastMinutes(self, n: int) -> int:
        dp = [0]*100
        dp[0]=0
        dp[1]=1
        dp[2]=2
        dp[3]=4
        cnt = 3
        while  dp[cnt]*2<=1e5:
            dp[cnt+1]=dp[cnt]*2
            cnt+=1
        dp[cnt+1] = 1e5
        ans = bisect.bisect_left(dp[:cnt+2],n)
        print(dp)
        return ans

s = Solution()
n = 100000
print(s.leastMinutes(n))