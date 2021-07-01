#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1786.py
# Author: WangYu
# Date  : 2021/3/8

from collections import defaultdict
from typing import List
import heapq

# class Solution:
#     def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
#         edge = defaultdict(dict)  # 既是邻接矩阵，又是邻接表
#         for x, y, weight in edges:
#             edge[x][y] = weight
#             edge[y][x] = weight
#         # n为源点，dijkstra单源最短路径,n到各点的最短距离，就是各点到n的最短距离
#         dist = [0x3f3f3f3f for _ in range(n + 1)]
#         dist[n] = 0
#         visited = set()
#         minHeap = [(0, n)]
#         while minHeap:
#             cloestDist, cloestNode = heapq.heappop(minHeap)  # 距离源节点最近的结点
#             if cloestNode in visited:  # 已经在选中的区域里了，就不要再选了
#                 continue
#             visited.add(cloestNode)  # 未选择的点中，这是最小的。正式加入区域
#             for nxt in edge[cloestNode].keys():  # 更新与它相连接的点
#                 if dist[cloestNode] + edge[cloestNode][nxt] < dist[nxt]:
#                     dist[nxt] = dist[cloestNode] + edge[cloestNode][nxt]
#                     heapq.heappush(minHeap, (dist[nxt], nxt))  # 有更小的了，就进minHeap
#         # 动态规划 dp  更多的是一种贪心！！！！！！！！！
#         dp = [0 for _ in range(n + 1)]
#         dp[n] = 1
#         a = [node for node in range(1, n + 1)]
#         a.sort(key=lambda x: dist[x])
#
#         for node in a:
#             for nxt in edge[node].keys():
#                 if dist[node] > dist[nxt]:
#                     dp[node] += dp[nxt]
#
#             if node == 1:  # a中右侧的点，距离都比1的远了，1的最短路径不可能经过他们到达n
#                 break
#
#         return dp[1] % (10 ** 9 + 7)
import collections
import functools
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = 10**9 + 7
        g = collections.defaultdict(list)
        for u, v, w in edges:
            g[u].append([v, w])
            g[v].append([u, w])
        q = [(0, n)]
        dist = [-1] * (n + 1)
        while q:
            dis, node = heapq.heappop(q)
            if dist[node] >= 0:
                continue
            dist[node] = dis

            for nn, wi in g[node]:
                heapq.heappush(q, [dis + wi, nn])

        @functools.lru_cache(None)
        def dfs(cur):
            if cur == n:
                return 1
            ans = 0
            for nn, wi in g[cur]:
                if dist[nn] < dist[cur]:
                    ans += dfs(nn)
            return ans

        return dfs(1) % mod


n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
s = Solution()
print(s.countRestrictedPaths(n,edges))