#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : niuke4.py
# Author: WangYu
# Date  : 2021/1/22
from functools import lru_cache

lru_cache(None)
def gao(n):
    if n == 1:
        return 0
    return n//2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        ans += gao(i)
    print(ans)


if __name__ == '__main__':
    main()