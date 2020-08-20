#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Leetcode529.py
# Author: WangYu
# Date  : 2020-08-20
'''
给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板

来源：力扣（LeetCode）
'''
class Solution:
    def updateBoard(self, board, click):
        r_len = len(board)
        c_len = len(board[0])
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        def calc(r, c):
            cnt = 0
            for d_r,d_c in direction:
                row = r + d_r
                col = c + d_c
                if (row >= 0 and row <r_len) and (col >= 0 and col <c_len) and board[row][col] == 'M':
                    cnt = cnt + 1
            return cnt
        def dfs(r,c):
            if board[r][c] == 'E':
                cnt = calc(r,c)
                if cnt != 0:
                    board[r][c] = str(cnt)
                    return
                board[r][c] = 'B'
                for d_r,d_c in direction:
                    row = r + d_r
                    col = c + d_c
                    if (row  >= 0 and row  < r_len) and (col >= 0 and c + d_c < c_len) and board[row][col] != 'M':
                        cnt = calc(row , col)
                        if cnt > 0:
                            board[row][col] = str(cnt)
                        elif cnt == 0:
                            dfs(row , col)
            return
        if len(click) == 2 and isinstance(click[0], int):
            if board[click[0]][click[1]] == 'M':
                board[click[0]][click[1]] = 'X'
                return board
            if board[click[0]][click[1]] == 'E':
                dfs(click[0], click[1])
        else:
            for r, c in click:
                if board[r][c] == 'M':
                    board[r][c] = 'X'
                    return board
                if board[r][c] == 'E':
                    dfs(r,c)
        return board

board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]

Click = [3,0]
s = Solution()
s.updateBoard(board,Click)





