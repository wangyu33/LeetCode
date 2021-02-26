#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : niuke6.py
# Author: WangYu
# Date  : 2021/1/28

from functools import lru_cache

lru_cache()
def a(n,k):
    ans = 1
    for i in range(k+1,n+1):
        ans = (ans *(i))
        if ans > pow(10,9)+7:
            ans = ans % (pow(10,9)+7)

    return ans

lru_cache()
def c(n,k):
    return a(n,k)/j(n-k)%(pow(10,9)+7)

lru_cache()
def j(n):
    if n==1 or n==0:
        return 1
    if n*j(n-1) > pow(10,9)+7:
        return  n*j(n-1) %(pow(10,9)+7)
    return n*j(n-1)

def main():
        t = int(input())
        for i in range(t):
            n,k = list(map(int, input().split()))
            ans = int(c(n,k))
            print(ans)

if __name__ == '__main__':
    main()