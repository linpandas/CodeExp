#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j]表示第i-1为结尾的word1和j-1为结尾的word2
        # 转换成相同的所使用的最小操作数
        dp = [[0]*(n+1) for _ in range(m+1)]
        # 初始化：当word1为空串时，以i-1为结尾的word2需要操作i次
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + 1
        # 同理，当word2为空串时，以j-1为结尾的word1需要操作j次
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[-1][-1]
# @lc code=end

