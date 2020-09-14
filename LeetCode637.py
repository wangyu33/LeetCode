#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode637.py
# Author: WangYu
# Date  : 2020-09-12


from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        tree_tuple = [(root,0)]
        mean = []
        while tree_tuple:
            temp = []
            ans = 0
            for node in tree_tuple:
                if node[0].left:
                    temp.append((node[0].left, node[1] + 1))
                if node[0].right:
                    temp.append((node[0].right, node[1] + 1))
                ans += node[0].val
            mean.append(ans/len(tree_tuple))
            tree_tuple = temp[:]
        return mean


s = Solution()
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
print(s.averageOfLevels(t))
