#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode538.py
# Author: WangYu
# Date  : 2020-09-21

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return []
        tree = [root]
        val = []
        while tree:
            tree_temp = tree[0]
            tree.pop(0)
            val.append(tree_temp.val)
            if tree_temp.left:
                tree.append(tree_temp.left)
            if tree_temp.right:
                tree.append(tree_temp.right)
        tree = [root]
        while tree:
            tree_temp = tree[0]
            if tree_temp.left:
                tree.append(tree_temp.left)
            if tree_temp.right:
                tree.append(tree_temp.right)
            temp = copy.deepcopy(tree_temp.val)
            for i in val:
                if i > temp:
                    tree_temp.val += i
            tree.pop(0)
        return root