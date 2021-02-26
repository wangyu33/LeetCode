#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode144.py
# Author: WangYu
# Date  : 2020/10/27

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        if not root.left and not root.right:
            return [root.val]
        ans.append(root.val)
        if root.left:
            ans.extend(self.preorderTraversal(root.left))
        # ans.append(root.val)
        if root.right:
            ans.extend(self.preorderTraversal(root.right))
        return ans