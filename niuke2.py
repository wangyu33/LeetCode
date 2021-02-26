#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : niuke2.py
# Author: WangYu
# Date  : 2021/1/22
'''
现在有n个物品，每一个物品都有一个价值，现在想将这些物品分给两个人，要求这两个人每一个人分到的物品的价值总和相同（个数可以不同，总价值相同即可），剩下的物品就需要扔掉，现在想知道最少需要扔多少价值的物品才能满足要求分给两个人。

输入描述:
第一行输入一个整数 T，代表有 T 组测试数据。

对于每一组测试数据，一行输入一个整数 n ，代表物品的个数。

接下来 n 个数，a[i] 代表每一个物品的价值。

1<= T <= 10
1 <= n <= 15
1 <= a[i] <= 100000
'''
from queue import Queue
from copy import deepcopy
from functools import lru_cache

lru_cache(None)


def dfs(l, r, n):
    global a, ans, asum, asum0
    if l == r:
        ans = min(ans, asum0 - l*2)
    if n == len(a):
        return
    # if ans < asum0 - l - r:
    #     return
    if l + a[n] <= asum:
        dfs(l + a[n], r, n + 1)
    if r + a[n] <= asum:
        dfs(l, r + a[n], n + 1)
    # dfs(l + a[n], r, n + 1)
    # dfs(l, r + a[n], n + 1)
    dfs(l, r, n + 1)


def main():
    global a, ans, asum, asum0
    T = int(input())
    for t in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        a = sorted(a, reverse=True)
        ans = sum(a)
        asum0 = sum(a)
        asum = asum0 // 2
        dfs(0, 0, 0)
        print(ans)


if __name__ == '__main__':
    main()