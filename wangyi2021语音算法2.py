#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : wangyi2021语音算法2.py
# Author: WangYu
# Date  : 2021/7/2
def judge(mid,E, EM, M, MH, H):
    if E < mid:
        EM -= (mid-E)
        E += (mid-E)
    if H<mid:
        MH -= (mid-H)
        H += (mid-E)
    if MH>=0 and EM>=0 and MH+EM+M>=mid:
        return True
    return False


if __name__ == '__main__':
    while True:
        try:
            [E, EM, M, MH, H] = list(map(int, input().split()))
            r = (E+EM+M+MH+H)//3
            l = 0
            ans = 0
            while l <= r:
                mid = (r+l)//2
                if judge(mid,E, EM, M, MH, H) == True:
                    l = mid +1
                    ans = max(ans,mid)
                else:
                    r = mid-1
            print(ans)
        except:
            break