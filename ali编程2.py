#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ali编程2.py
# Author: WangYu
# Date  : 2021/7/2

mod = 1e9+7
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        [a,b,n] = list(map(int, input().split()))
        dp = [0]* (n+1)
        dp[0] = 2
        dp[1] = a%mod
        dp[2] = (a * a % mod - 2 * b % mod + mod) % mod
        for i in range(3,n+1):
            dp[i] = ((a*dp[i-1]%mod)-(b*dp[i-2]%mod)+mod)%mod
        print(int(dp[-1]))