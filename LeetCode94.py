#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode94.py
# Author: WangYu
# Date  : 2020-09-14

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        tree_tuple = [(root,0)]
        ans = []
        while tree_tuple:
            tree, flag = tree_tuple.pop()
            if flag == 0:
                if tree.right:
                    tree_tuple.append((tree.right, 0))
                tree_tuple.append((tree, 1))
                if tree.left:
                    tree_tuple.append((tree.left, 0))
            else:
                ans.append(tree.val)
        return ans


s = Solution()
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
print(s.inorderTraversal(t))
