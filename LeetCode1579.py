#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1579.py
# Author: WangYu
# Date  : 2021/1/27


from typing import List
from collections import  defaultdict


def find(x, fa):
    if fa[x] == x:
        return fa[x]
    fa[x] = find(fa[x], fa)
    return fa[x]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        fa = {i:i for i in range(1,n+1)}
        fb = {i:i for i in range(1,n+1)}
        ans = 0
        for i in edges:
            if i[0] == 3:
                a,b = find(i[1],fa),find(i[2],fa)
                if a == b:
                    ans += 1
                else:
                    fa[b] = a
                    fb[b] = a
                continue
            a,b = max(i[1], i[2]), min(i[1], i[2])
            edge = (a,b)
            d[edge].append(i[0])
        d = sorted(d.items(), key = lambda x:len(x[1]), reverse = True)
        for edge, node_type in d:
            a,b = find(edge[0], fa),find(edge[1], fa)
            c,d = find(edge[0], fb),find(edge[1], fb)
            if a == b and c == d:
                ans += len(node_type)
            else:
                if 2 in node_type:
                    if c == d:
                        ans += 1
                    else:
                        fb[d] = c
                if 1 in node_type:
                    if a==b:
                        ans+=1
                    else:
                        fa[b] = a
        flaga = 0
        flagb = 0
        for i in range(1,n+1):
            if i == 1:
                flaga = find(i,fa)
                flagb = find(i,fb)
            elif flaga != find(i,fa) or flagb != find(i,fb):
                return 0
        return ans

# n = 4
# edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
n = 7
edges = [[2,1,2],[3,1,3],[2,3,4],[2,2,5],[2,5,6],
         [3,5,7],[3,2,5],[2,3,5],[1,2,7],[1,5,7],
         [3,6,7],[1,1,3],[1,2,3],[3,1,5],[2,1,5],
         [3,2,3],[2,2,6],[1,2,5],[3,3,7],[1,2,6],
         [2,5,7],[1,3,7],[3,1,2],[3,2,7],[1,1,5],
         [2,2,4],[2,1,6],[3,1,4],[2,2,7],[2,1,7],
         [3,5,6],[1,4,5]]
s = Solution()
print(s.maxNumEdgesToRemove(n,edges))