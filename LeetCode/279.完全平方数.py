#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1) # 和为j的完全平方数的最小数量为dp[j]
        dp[0] = 0
        for i in range(1, int(n**0.5)+1):
            for j in range(i*i, n+1):
                dp[j] = min(dp[j], dp[j - i*i] + 1)
        
        return dp[-1]
# @lc code=end

