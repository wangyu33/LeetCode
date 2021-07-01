#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1824.py
# Author: WangYu
# Date  : 2021/4/12

from typing import List
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)

        dp = [[float('inf') for _ in range(3)] for _ in range(n)]
        ############## dp，从左往右
        dp[0][0] = 1
        dp[0][1] = 0
        dp[0][2] = 1

        for i in range(n - 1):
            for j in range(3):
                ## 如果可以从隔壁跑道移动过来更优，就移动
                dp[i][j] = min(dp[i][j], min(dp[i]) + 1)

                ## 往右推
                if obstacles[i] != 1 and obstacles[i + 1] != 1:
                    dp[i + 1][0] = dp[i][0]
                if obstacles[i] != 2 and obstacles[i + 1] != 2:
                    dp[i + 1][1] = dp[i][1]
                if obstacles[i] != 3 and obstacles[i + 1] != 3:
                    dp[i + 1][2] = dp[i][2]

        return min(dp[n - 1])

obstacles = [0,1,2,3,0]
s = Solution()
print(s.minSideJumps(obstacles))