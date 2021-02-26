#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1705.py
# Author: WangYu
# Date  : 2021/1/21
from typing import List
import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        for i in range(len(apples)):
            days[i] += i
        ans = 0
        q = []
        #  n = max([i + days[i] for i in range(len(days))]) + 1
        # while len(apples) < n:
        #     apples.append(0)
        #     days.append(0)
        # for i in range(n):
        #     if apples[i] > 0:
        #         heapq.heappush(q, (i + days[i], apples[i]))
        #     while len(q) > 0:
        for i in range(max(days)):
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(q, (days[i], apples[i]))
            while len(q) > 0:
                x, y = heapq.heappop(q)
                if x > i:
                    ans += 1
                    if y > 1:
                        heapq.heappush(q, (x, y - 1))
                    break
        return ans

s = Solution()
a =[1,2,3,5,2]
b = [3,2,1,4,2]
print(s.eatenApples(a,b))