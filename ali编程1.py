#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ali编程1.py
# Author: WangYu
# Date  : 2021/7/2

from bisect import bisect_left
T = int(input())
for _ in range(T):
    n = int(input())
    X = map(int, input().split())
    Y = map(int, input().split())
    a = sorted(zip(X, Y), key=lambda x: (x[0], -x[1]))
    total = 0
    q = [0] * 100005
    for i in range(n):
        t = bisect_left(a=q, x=a[i][1], lo=0, hi=total)
        if t == total:
            total += 1
        q[t] = a[i][1]
    print(total)