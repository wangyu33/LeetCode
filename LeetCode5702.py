#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5702.py
# Author: WangYu
# Date  : 2021/3/14

import collections
from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        maxn = 0
        idx = -1
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            print(edges[i])
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
            if len(graph[edges[i][0]]) > maxn:
                maxn = len(graph[edges[i][0]])
                idx = graph[edges[i][0]]
            if len(graph[edges[i][1]]) > maxn:
                maxn = len(graph[edges[i][1]])
                idx = graph[edges[i][1]]
        return idx