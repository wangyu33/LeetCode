#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : yxh.py
# Author: WangYu
# Date  : 2021/3/12

from collections import defaultdict
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n,m = list(map(int,input().split()))
        D = defaultdict(int)
        node = []
        for i in range(m):
            x,y = list(map(int,input().split()))
            node.append([x,y])
            D[x] = y
        for x,y in node:
            if D[]
