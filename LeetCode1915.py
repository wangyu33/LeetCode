#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1915.py
# Author: WangYu
# Date  : 2021/6/28

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [0] * (1<<10)
        cnt[0] += 1
        ret = 0
        cur = 0
        for i in range(len(word)):
            cur ^= (1<<(ord(word[i])-ord('a')))
            for j in range(10):
                tmp = cur^(1<<j)
                ret += cnt[cur^(1<<j)]
            ret += cnt[cur]
            cnt[cur] += 1
        return ret

word = "aba"
s = Solution()
print(s.wonderfulSubstrings(word))