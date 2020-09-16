#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode226.py
# Author: WangYu
# Date  : 2020-09-16

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        def gao(tree):
            if not tree.left and not tree.right:
                return tree
            if tree.left:
                gao(tree.left)
            if tree.right:
                gao(tree.right)
            tree.left, tree.right = tree.right, tree.left
            return tree
        return gao(root)
