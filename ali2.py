#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ali2.py
# Author: WangYu
# Date  : 2021/3/22
from functools import lru_cache
@lru_cache(None)
def dp(i,j):
    if i>j:
        return 0
    if j - i <= 1:
        return d[i][j]
    summ = sum(arr[i:j+1])
    maxn = 0
    s = 0
    for k in range(i,j+1):
        s = s+arr[k]
        if s < summ -s:
            maxn = max(maxn, s + dp(i,k))
        elif s> summ - s:
            maxn = max(maxn, summ - s + dp(k+1,j))
        else:
            maxn = max(maxn, s + dp(i,k), summ - s + dp(k+1,j))
    return maxn

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    d = [[0] * len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        d[i][i] = arr[i]
        if i+1 < len(arr):
            d[i][i+1] = min(arr[i:i+2])
    print(dp(0,len(arr)-1))
    dp.cache_clear()
