#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode557.py
# Author: WangYu
# Date  : 2020-08-30

class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(' ')
        ans = []
        for temp in str_list:
            ans.append(temp[::-1])
        return ' '.join(ans)

s1 = Solution()
s2 = "Let's take LeetCode contest"
print(s1.reverseWords(s2))