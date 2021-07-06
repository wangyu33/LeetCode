#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5801.py
# Author: WangYu
# Date  : 2021/7/5

from typing import List
import heapq
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i in range(len(dist)):
            dist[i] = dist[i]/speed[i]
        dist = sorted(dist)
        cnt = 0
        for i in range(len(dist)):
            if dist[i] > i:
                cnt +=1
            else:
                return cnt
        return cnt

dist = [4,2,8]
speed =[2,1,4]
s = Solution()
print(s.eliminateMaximum(dist, speed))