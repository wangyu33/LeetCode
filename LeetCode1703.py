#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1703.py
# Author: WangYu
# Date  : 2021/1/23

from typing import List
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        n = len(nums)
        g, total, count = list(), [0], -1

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
                g.append(i - count)
                total.append(total[-1] + g[-1])

        m, ans = len(g), float("inf")

        for i in range(m - k + 1):
            mid = (i + i + k - 1) // 2
            q = g[mid]
            ans = min(ans, (2 * (mid - i) - k + 1) * q + (total[i + k] - total[mid + 1]) - (total[mid] - total[i]))

        return ans

s = Solution()
nums = [1,0,0,1,0,1]
k = 2
print(s.minMoves(nums,k))