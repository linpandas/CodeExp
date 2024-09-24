#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        n = len(prices)
        # dp[i][0]表示第i天持有股票所得最多现金
        # dp[i][1]表示第i天不持有股票所得最多现金
        dp = [[0, 0] for _ in range(n)]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        
        return dp[-1][1]

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 贪心算法
#         low = float("inf")
#         result = 0
#         for price in prices:
#             low = min(low, price)
#             result = max(result, price-low)
        
#         return result
# @lc code=end

