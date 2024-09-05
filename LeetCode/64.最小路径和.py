#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = sum([grid[x][0] for x in range(i+1)])
        for j in range(n):
            dp[0][j] = sum([grid[0][x] for x in range(j+1)])
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

        return dp[-1][-1]
# @lc code=end

