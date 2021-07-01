#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Vivo3.py
# Author: WangYu
# Date  : 2021/4/1

from collections import defaultdict
def judge(a,b,n):
    if a<0 or b<0 or a>=n or b>=n:
        return False
    return True

if __name__ == '__main__':
    n = int(input())
    s1,s0, t1,t0 = list(map(int,input().split()))
    graph = []
    for i in range(n):
        graph.append(input())
    visit = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '#' or graph[i][j] == '@':
                visit[(i,j)] = 1
    node = [(s0,s1)]
    visit[(s0,s1)] = 1
    flag = 0
    cnt = 0
    while node:
        tmp = []
        if flag == 1:
            break
        for x,y in node:
            if flag == 1:
                break
            for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
                if flag == 1:
                    break
                if judge(x+a, y+b, n) and visit[(x+a,y+b)] == 0:
                    if (x+a) == t0 and (y+b) == t1:
                        flag = 1
                    tmp.append((x+a,y+b))
                    visit[(x+a,y+b)]=1
        node = tmp
        cnt += 1
    if flag:
        print(cnt)
    else:
        print(-1)