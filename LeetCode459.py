#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode459.py
# Author: WangYu
# Date  : 2020-08-24

'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-substring-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        t = len(s)
        import math
        for i in range(1,int(math.sqrt(t)) + 2):
            if t % i == 0:
                if i < t and s[:i] * (t // i) == s:
                    return True
                if i != 1 and s[:(t // i)] * i == s:
                    return True
        return False

s = Solution()
str = "ab"
print(s.repeatedSubstringPattern(str))
