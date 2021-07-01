#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode815.py
# Author: WangYu
# Date  : 2021/6/28

from typing import List
from collections import  defaultdict
import collections
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        n = len(routes)
        car = defaultdict(set)
        for i in range(n):  # 线路i
            for y in routes[i]:  # 站点y
                car[y].add(i)

        # -------------------------- bfs波纹法
        Q = collections.deque()
        visited = [False for _ in range(n)]
        for i in car[source]:
            Q.append(i)
            visited[i] = True  # 没辆车就坐1次
        step = 0
        while Q:
            cur_len = len(Q)
            for _ in range(cur_len):
                i = Q.popleft()  # 线路i
                for y in routes[i]:  # 可到达的站点y
                    if y == target:
                        return step + 1
                    for j in car[y]:  # 想要到达站点y，上可到达y的车
                        if visited[j] == False:
                            visited[j] = True
                            Q.append(j)
            step += 1

        return -1

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source = 15
target = 12
s = Solution()
print(s.numBusesToDestination(routes,source,target))