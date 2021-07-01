#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1839.py
# Author: WangYu
# Date  : 2021/4/26

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        l = 0
        r = 1
        maxn = 0
        while l < len(word) and r < len(word):
            if word[r] >= word[r-1]:
                r += 1
            else:
                if r-l>=5 and all(('a' in word[l:r], 'e' in word[l:r],'i' in word[l:r],'o' in word[l:r],'u' in word[l:r])):
                    maxn = max(maxn,r-l)
                l = r
                r = r+1
        return maxn

word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
s = Solution()
print(s.longestBeautifulSubstring(word))