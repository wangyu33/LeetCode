#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode486.py
# Author: WangYu
# Date  : 2020-09-01

'''
给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/predict-the-winner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        #递归
        # def gao(start,end, flag):
        #     if start == end:
        #         return nums[start] * flag
        #     score_start = nums[start] * flag + gao(start + 1, end, - flag)
        #     score_end = nums[end] * flag + gao(start, end - 1, - flag)
        #     return max(score_start * flag,  score_end * flag) * flag
        # return gao(0, len(nums)-1, 1) >= 0

        #dp
        # length = len(nums)
        # dp = [[0] * length for _ in range(length)]
        # for i, num in enumerate(nums):
        #     dp[i][i] = num
        # for i in range(length - 2, -1, -1):
        #     for j in range(i + 1, length):
        #         dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        # return dp[0][length - 1] >= 0

        #记忆化搜索
        dp = [[-1]*21 for _ in range(len(nums))]
        def dfs(l,r):
            if dp[l][r] != -1:
                return dp[l][r]
            if l == r:
                dp[l][r] = nums[l]
                return dp[l][r]
            dp[l][r] = sum(nums[l:r + 1]) - min(dfs(l+1,r), dfs(l,r-1))
            return dp[l][r]
        return dfs(0,len(nums) - 1) * 2 >= sum(nums)





s = Solution()
nums = [3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]
print(s.PredictTheWinner(nums))
