#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : tencent1.py
# Author: WangYu
# Date  : 2021/3/4
'''小Q的父母要出差N天，走之前给小Q留下了M块巧克力。小Q决定每天吃的巧克力数量不少于前一天吃的一半，但是他又不想在父母回来之前的某一天没有巧克力吃，请问他第一天最多能吃多少块巧克力

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，表示父母出差的天数N(N<=50000)和巧克力的数量M(N<=M<=100000)。'''
import bisect


def gao(n, m):
    ret = 0
    for i in range(n):
        ret += m
        m = (m + 1) // 2
    return ret


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    l, r = 1, m
    while l < r:
        mid = (l + r + 1) // 2
        tmp = gao(n, mid)
        if tmp > m:
            r = mid - 1
        elif tmp < m:
            l = mid
        else:
            l = mid
            break
    print(l)