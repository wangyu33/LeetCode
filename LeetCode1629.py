#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1629.py
# Author: WangYu
# Date  : 2020/10/26

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        t = [releaseTimes[0]]
        for i in range(len(releaseTimes) - 1):
            t.append(releaseTimes[i + 1] - releaseTimes[i])
        d = defaultdict(int)
        maxn = 0
        maxch = ''
        for ch in range(len(keysPressed)):
            if keysPressed[ch] in d:
                d[ch] += t[ch]
            else:
                d[ch] = t[ch]

            if d[ch] > maxn:
                maxn = d[ch]
                maxch = keysPressed[ch]
            elif d[ch] == maxn:
                maxch = keysPressed[ch] if ord(keysPressed[ch]) > ord(maxch) else maxch
        return maxch