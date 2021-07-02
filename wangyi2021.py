#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : wangyi2021.py
# Author: WangYu
# Date  : 2021/7/2


from collections import defaultdict


def dfs(cnt, d, index):
    global minn, a
    if minn != 1<<31:
        return
    if cnt == 0:
        tmp = 0
        for i in range(len(a)):
            if d[i] == 0:
                tmp+= a[i]
        minn = min(minn,tmp)
        return
    if cnt<0:
        return

    for i in range(index, len(d)):
        if d[i] == 0:
            d1 = d[:]
            d1[i] = 1
            dfs(cnt-a[i],d1, i+1)
            dfs(cnt,d[:],i+1)




if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        summ = sum(a)
        minn = 1 << 31
        cnt = [(0, [0] * len(a))]
        for i in range(len(a)):
            tmp = []
            for c, d in cnt:
                tmp.append((c, d))
                c += a[i]
                d1 = d[:]
                d1[i] = 1
                if c < summ / 2:
                    tmp.append((c, d1))
            cnt = tmp
        cnt = sorted(cnt, key=lambda x: (x[0]), reverse=True)
        d = defaultdict(int)
        for c,flag in cnt:
            if d[c]==0:
                dfs(c,flag,0)
                d[c]=1
                if minn != 1<<31:
                    break
        print(minn)





