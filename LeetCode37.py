#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode37.py
# Author: WangYu
# Date  : 2020-09-15

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[[0] * 9 for _a in range(3)] for _b in range(3)]
        flag = [0]
        space = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    space.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = 1
        ans = []

        def dfs(index):
            if index == len(space) and flag[0] == 0:
                flag[0] = 1
                print(board)
                return
            if flag[0] == 1:
                return
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for digit in range(9):
                            if row[i][digit] == 0 and col[j][digit] == 0 and block[i // 3][j // 3][digit] == 0:
                                board[i][j] = str(digit + 1)
                                row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = 1
                                dfs(index + 1)
                                if flag[0] == 1:
                                    return
                                board[i][j] = '.'
                                row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = 0
                        return

        dfs(0)

s = Solution()
m = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(m)



