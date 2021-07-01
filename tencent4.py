#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : tencent4.py
# Author: WangYu
# Date  : 2021/3/4

def fac(n):
    ans = 1
    for i in range(n):
        ans = (ans * i) % 1000000007
    return ans
def c(i,n):
    if i == 0:
        return 1
    if i == 1:
        return n
    return fac(n)/fac(i)/fac(n-i)
if __name__ == '__main__':
    n = int(input())
    a,x,b,y = list(map(int,input().split()))
    cnt = 0
    for i in range(x):
        tmp = n - a*i
        if tmp % b == 0 and tmp/b <= y:
            cnt = cnt + c(i,x)*c(tmp//b,y)
            cnt = cnt % 1000000007
    print(cnt)