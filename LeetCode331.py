#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode331.py
# Author: WangYu
# Date  : 2021/3/12

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        global flag
        flag = 1
        def dfs(preorder):
            global flag
            if len(preorder) == 0 or flag == 0:
                flag = 0
                return
            ch = preorder.pop(0)
            if ch == '#':
                return
            dfs(preorder)
            dfs(preorder)
        dfs(preorder)
        if len(preorder) > 0:
            return False
        return flag==1

pre = "1,#,#,1"
s = Solution()
print(s.isValidSerialization(pre))