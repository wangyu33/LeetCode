#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1035.py
# Author: WangYu
# Date  : 2021/4/1

from typing import List

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        from collections import defaultdict
        dp = [[0]* (len(B)+1) for _ in range(len(A)+1)]
        ret = 0
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                print(A[i-1],B[j-1])
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                ret = max(ret,dp[i][j])
        return ret


A = [1,3,7,1,7,5]
B = [1,9,2,5,1]
s = Solution()
print(s.maxUncrossedLines(A,B))