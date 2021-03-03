#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5692.py
# Author: WangYu
# Date  : 2021/3/1

from typing import List
import heapq
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        def cal(car1, car2):
            if car1[1] <= car2[1]:
                return -1
            return (car2[0] - car1[0]) / (car1[1] - car2[1])

        queue = []
        n = len(cars)
        ans = [-1] * n

        mapping = {i: i - 1 for i in range(n)}

        for i in range(n - 1):
            tmp = cal(cars[i], cars[i + 1])
            if tmp != -1:
                heapq.heappush(queue, (tmp, i, i + 1))

        while queue:
            time, left, right = heapq.heappop(queue)
            if ans[left] != -1:
                continue
            ans[left] = time
            mapping[right] = mapping[left]
            if mapping[left] == -1:
                continue
            new = mapping[left]
            tmp = cal(cars[new], cars[right])
            if tmp != -1:
                heapq.heappush(queue, (tmp, new, right))

        return ans

cars = [[1,2],[2,1],[4,3],[7,2]]
s = Solution()
print(s.getCollisionTimes(cars))