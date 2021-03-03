#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : meituan1.py
# Author: WangYu
# Date  : 2021/3/1

if __name__ == '__main__':
    while True:
        try:
            n,m,h,l = list(map(int,input().split()))
            now = list(map(int, input().split()))
            H = max(h,l)
            L = min(h,l)
            H_flag = 1
            L_flag = 1
            flag = 1
            for i in now:
                if i > H:
                    flag = 0
                    break
                elif i < L:
                    flag = 0
                    break
                elif i == H:
                    H_flag = 0
                elif i == L:
                    L_flag = 0
            if flag == 0:
                print("NO")
            else:

                if n - m >= H_flag + L_flag:
                    print('Yes')
                else:
                    print('NO')
        except:
            break