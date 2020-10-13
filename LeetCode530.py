#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode530.py
# Author: WangYu
# Date  : 2020-10-12

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        tree = [root]
        ans = []
        while tree:
            temp = []
            for t in tree:
                if t.left:
                    temp.append(t.left)
                if t.right:
                    temp.append(t.right)
                ans.append(t.val)
            tree = temp
        ans = sorted(ans)
        print(ans)
        cha = 1000000
        for i in range(len(ans)-1):
            cha = min(abs(ans[i]-ans[i+1]), cha)
        return cha