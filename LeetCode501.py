#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode501.py
# Author: WangYu
# Date  : 2020-09-24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        d = defaultdict(int)
        tree = [root]
        while tree:
            temp = tree[0]
            tree.pop(0)
            d[temp.val] += 1
            if temp.left:
                tree.append(temp.left)

            if temp.right:
                tree.append(temp.right)
        maxn = 0
        ans = []
        for i in d:
            if d[i] > maxn:
                maxn = d[i]
                ans = []
                ans.append(i)
            if d[i] == maxn and i not in ans:
                ans.append(i)
        return ans