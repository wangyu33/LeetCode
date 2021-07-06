#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : TZOJ1005.py
# Author: WangYu
# Date  : 2021/7/5

if __name__ == '__main__':
    while True:
        try:
            [a,b,c] = list(map(int,input().split()))
            print(pow(a,b,c))
        except:
            break