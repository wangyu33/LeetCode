#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ali1.py
# Author: WangYu
# Date  : 2021/3/22
import sys
def dfs(w, index, target):
    global flag
    if flag == 1:
        return
    if target == 0:
        flag = 1
        return
    if index >= len(w) or sum(w[index:]) < target or target < 0:
        return
    dfs(w, index + 1, target - w[index])
    dfs(w, index + 1, target)


if __name__ == '__main__':
    while True:
        try:
            n, m = list(map(int, input().split()))
            w = list(map(int, input().split()))
            global flag
            flag = 0
            w = sorted(w, reverse=True)
            dfs(w, 0, m)
            if flag == 1:
                print('YES')
            else:
                print('NO')
        except:
            break