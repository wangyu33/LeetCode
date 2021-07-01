#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LCP7.py
# Author: WangYu
# Date  : 2021/7/1

from typing import List
from collections import defaultdict
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        g = defaultdict(list)
        cnt = 0
        for i in range(len(relation)):
            g[relation[i][0]].append(relation[i][1])

        def dfs(index, player):
            nonlocal cnt
            if index == k - 1 and n - 1 in g[player]:
                cnt += 1
                return
            elif index == k - 1 and n - 1 not in g[player]:
                return
            for i in g[player]:
                dfs(index + 1, i)

        dfs(0, 0)
        return cnt

s = Solution()
n = 5
relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
k = 3
print(s.numWays(n,relation,k))
