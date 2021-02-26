#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : niuke7.py
# Author: WangYu
# Date  : 2021/1/28

from math import ceil


def solve(t, num, a, b):
    num_a = 0
    for i in t:
        num_a += ceil(max(0,(i - num * b) / a))
    return num_a > num


def main():
    n, a, b = list(map(int, input().split()))
    t = list(map(int, input().split()))
    l = 1
    r = 1e9
    while l < r:
        mid = (l + r) // 2
        if solve(t, mid, a, b):
            l = mid + 1
        else:
            r = mid
    print(int(l))


if __name__ == '__main__':
    main()