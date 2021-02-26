#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : zjtd 1.py
# Author: WangYu
# Date  : 2021/2/24

if __name__ == '__main__':
    n = int(input())
    point = []
    for i in range(n):
        a,b = list(map(int, input().split()))
        point.append((a,b))
    point = sorted(point,key = lambda x:x[0])
    maxn = [-1] * (len(point)+1)
    for i in range(len(point)-1,-1,-1):
        maxn[i] = max(maxn[i+1],point[i][1])
    for i in range(len(point)):
        if point[i][1]>maxn[i]:
            print(point[i][0],point[i][1])