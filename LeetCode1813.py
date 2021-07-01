#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1813.py
# Author: WangYu
# Date  : 2021/4/6

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        if len(sentence1) < len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        while sentence2 and sentence2[0] == sentence1[0]:
            sentence2.pop(0)
            sentence1.pop(0)
        while sentence2 and sentence2[-1] == sentence1[-1]:
            sentence2.pop(-1)
            sentence1.pop(-1)
        if len(sentence2) == 0:
            return True
        return False

s = Solution()
sentence1 = "of"
sentence2 = "A lot of words"
print(s.areSentencesSimilar(sentence1,sentence2))