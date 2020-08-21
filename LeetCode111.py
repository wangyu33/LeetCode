#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode111.py
# Author: WangYu
# Date  : 2020-08-21

'''给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        tree = [root]
        dict = {}
        dict[root] = 1
        while tree != None:
            if not tree[0].left and not tree[0].right:
                return dict[tree[0]]
            if tree[0].left:
                tree.append(tree[0].left)
                dict[tree[0].left] = dict[tree[0]] + 1
            if tree[0].right:
                tree.append(tree[0].right)
                dict[tree[0].right] = dict[tree[0]] + 1
            del dict[tree[0]]
            #删除第一个元素
            tree.pop(0)

s = Solution()
list = [3,9,20,'null','null',15,7]
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
print(s.minDepth(tree))


