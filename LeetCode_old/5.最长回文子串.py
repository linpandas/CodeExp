#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, maxL = 0, 1
        # dp[i][j]表示[i,j]内的子串是否为回文子串
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True
                        curL = j-i+1
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        curL = j-i+1
                if dp[i][j] and curL > maxL:
                    maxL = curL
                    start = i
        
        return s[start:start+maxL]
# @lc code=end

