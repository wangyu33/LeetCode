#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : meituan2.py
# Author: WangYu
# Date  : 2021/3/1

import bisect
if __name__ == '__main__':
    n,x = list(map(int, input().split()))
    p = list(map(int, input().split()))
    p = sorted(p, reverse=True)
    cnt = 0
    for i in p:
        if i != 0 and cnt <= x:
            cnt+= 1
        elif i!= 0 and cnt > x and i == p[cnt-1]:
            cnt += 1
    print(cnt)