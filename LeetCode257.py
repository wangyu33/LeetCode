#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode257.py
# Author: WangYu
# Date  : 2020-09-04

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        if root == None:
            return []
        def dfs(tree: TreeNode, s):
            if tree.left == None and tree.right == None:
                s = s + '->' + str(tree.val)
                ans.append(s)
            if tree.left:
                temp = '->' + str(tree.val)
                dfs(tree.left, s + temp)
            if tree.right:
                temp = '->' + str(tree.val)
                dfs(tree.right, s + temp)
        if root.left == None and root.right == None:
            return list(str(root.val))
        if root.left:
            dfs(root.left, str(root.val))
        if root.right:
            dfs(root.right, str(root.val))
        return ans

s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(5)
print(s.binaryTreePaths(t))





