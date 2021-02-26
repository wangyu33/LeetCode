#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : niuke5.py
# Author: WangYu
# Date  : 2021/1/22

'''
在一次聚会中，教授们被要求写下自己认可哪位教授的学术成果（也可以写自己，且可能出现重复）。已知，如果教授 A 认可教授 B ，且教授 B 认可教授 C，那么即可视为教授 A 也认可教授 C。现在我们想知道有多少对教授是两两互相认可的？

输入描述:
第一行两个正整数，教授人数 n，以及认可关系总数 m ；
接下来 m 行，每行两个正整数 x 和 y，表示教授 x 认可教授 y（x , y可能相等且可能出现重复）

输出描述:
一行一个数字表示答案，即互相认可的教授有多少对。

输入例子1:
5 6
1 3
2 1
3 2
3 5
4 5
5 4

输出例子1:
4
'''

from functools import lru_cache
from collections import defaultdict
from copy import deepcopy

def dfs(path, graph,circle):
    global flag
    root = path[0]
    if root in graph[path[-1]]:
        circle.append(path)
        for i in circle[-1]:
            flag[i] = 1
        return
    for i in graph[path[-1]]:
        if i in path:
            circle.append(path[path.index(i):])
            for i in circle[-1]:
                flag[i] = 1
        else:
            tmp = deepcopy(path)
            tmp.append(i)
            dfs(tmp, graph, circle)



def main():
    global flag
    n,m = list(map(int, input().split()))
    graph = defaultdict(list)
    circle = []
    ans = 0
    for i in range(m):
        a,b = list(map(int, input().split()))
        if a == b:
            continue
        graph[a].append(b)
    for i in range(1, n+1):
        graph[i] = list(set(graph[i]))
    flag = [0] * (n + 1)
    for i in range(1, n+1):
        if flag[i] == 0:
            dfs([i], graph, circle)

    flag1 = [0] * (n + 1)
    for i in circle:
        sum1 = 0
        for j in i:
            if flag1[j] == 0:
                flag1[j] = 1
            else:
                sum1 += 1
        if sum1 <= 1:
            ans += len(i) *(len(i)-1)/2
        else:
            ans = ans + len(i) *(len(i)-1)/2 - sum1*(sum1-1)/2
    print(int(ans))





if __name__ == '__main__':
    main()