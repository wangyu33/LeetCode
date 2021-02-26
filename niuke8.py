#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : niuke8.py
# Author: WangYu
# Date  : 2021/1/29

'''
牛牛要参加一场程序猿世界杯，一共有名选手参加比赛，选手们依次编号从到，比赛采用单淘汰制，
即第一轮进行比赛，第一轮的决胜者再与相连的选手进行比赛，每轮都会淘汰一半的选手，进行之后能决出冠军。
牛牛的编号为，但是牛牛知道了各个选手与其他选手比赛时的胜率。牛牛想知道他能夺冠的概率是多少呢，
牛牛给你各个选手之间若进行比赛时的胜率，请你告诉牛牛他夺冠可能的概率是多少呢
'''
# import numpy as np

if __name__ == '__main__':
    n,m = list(map(int, input().split()))
    m -= 1
    lines = 2**n
    matrix = []
    for i in range(lines):
        temp = list(map(float, input().split()))
        matrix.append([i/100 for i in temp])
    # matrix = np.array(matrix)
    ans = []
    line = []
    for i in range(0,lines,2):
        j = i+1
        if i==m:
            line.append([(i,matrix[i][j])])
            continue
        elif j == m:
            line.append([(j, matrix[j][i])])
            continue
        temp = []
        temp.append((i,matrix[i][j]))
        temp.append((j, matrix[j][i]))
        line.append(temp)
    ans.append(line)
    for t in range(n-1):
        line = []
        now = ans[-1]
        for i in range(0,len(now),2):
            j = i+1
            #处理小牛的情况
            if len(now[i]) == 1:
                cow = now[i][0]
                p = 0
                for k in now[j]:
                    p += cow[1] * matrix[cow[0]][k[0]] * k[1]
                line.append([(cow[0], p)])
                continue

            if len(now[j]) == 1:
                cow = now[j][0]
                p = 0
                for k in now[i]:
                    p += cow[1] * matrix[cow[0]][k[0]] * k[1]
                line.append([(cow[0], p)])
                continue

            temp = []
            for ii in now[i]:
                p = 0
                for jj in now[j]:
                    p+= ii[1] * jj[1] * matrix[ii[0]][jj[0]]
                temp.append((ii[0], p))
            for ii in now[j]:
                p = 0
                for jj in now[i]:
                    p+= ii[1] * jj[1] * matrix[ii[0]][jj[0]]
                temp.append((ii[0], p))

            line.append(temp)
        ans.append(line)
    print(ans[-1][0][0][1])



