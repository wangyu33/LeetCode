#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1722.py
# Author: WangYu
# Date  : 2021/1/20

from copy import deepcopy
from typing import List
from collections import Counter
import collections


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n=len(source)
        parent={i:i for i in range(n)}
        # 并查集
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        # 搜索根节点
        for l,r in allowedSwaps:
            a,b=find(l),find(r)
            if a!=b:
                parent[b]=a
        # 获取根节点对应的连通块
        dic=collections.defaultdict(list)
        for i in range(n):
            a=find(i)
            dic[a].append(i)
        res=0
        # 计算每个连通块对应的source元素与target的差集
        for k,v in dic.items():
            a=[source[i] for i in v]
            b=Counter([target[i] for i in v])
            for c in a:
                if b[c]>0:
                    b[c]-=1
                else:
                    res+=1
        return res

source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]

s = Solution()
s.minimumHammingDistance(source, target, allowedSwaps)