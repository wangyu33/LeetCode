#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : meituan3.py
# Author: WangYu
# Date  : 2021/3/1

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        res = a[0]
        pre = a[0]
        for i in range(1,n):
            if pre > 0:
                tmp = pre + a[i]
            else:
                tmp = a[i]
            pre = tmp
            res = max(res, tmp)
        pre = a[0]
        for i in range(1,n):
            if pre < 0:
                tmp = pre + a[i]
            else:
                tmp = a[i]
            pre = tmp
            res = max(res, sum(a) - tmp)
        print(res)