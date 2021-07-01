#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : meituan2021-8-2.py
# Author: WangYu
# Date  : 2021/3/15

if __name__ == '__main__':
    n = int(input())
    s = input()
    nums = []
    for i in range(n):
        if s[i] == 'E':
            nums.append(1)
        else:
            nums.append(-1)
    dp = [0] * n
    for i in range(n):
        if i == 0:
            dp[i] = max(0,nums[i])
        else:
            dp[i] = max(dp[i-1]+nums[i],0)
    print(max(dp))