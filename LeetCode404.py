#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode404.py
# Author: WangYu
# Date  : 2020-09-19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = [0]
        def dfs(tree):
            if not tree:
                return
            if tree.left and not tree.left.left and not tree.left.right:
                ans[0] += tree.left.val
            dfs(tree.left)
            dfs(tree.right)
        dfs(root)
        return ans[0]