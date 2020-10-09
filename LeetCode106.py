#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode106.py
# Author: WangYu
# Date  : 2020-09-25

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def dfs(in_l, in_r, post_l, post_r):
            if post_l < post_r:
                return None
            inorder_root = Hash[postorder[post_l]]

            root = TreeNode(postorder[post_l])
            subtree_size = in_r - inorder_root
            root.right = dfs(inorder_root+1, in_r, post_l-1, post_l-subtree_size)
            root.left = dfs(in_l, inorder_root-1, post_l-subtree_size-1, post_r)
            return root

        Hash = {key:value for value, key in enumerate(inorder)}
        return dfs(0, len(inorder)-1, len(postorder)-1, 0)
