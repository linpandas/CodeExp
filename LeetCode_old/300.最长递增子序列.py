#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # dp[i]表示i之前的包括i的以nums[i]为结尾的最长递增序列的长度
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 注意这里不是要dp[i] 与 dp[j] + 1进行比较，
                    # 而是我们要取dp[j] + 1的最大值。
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
# @lc code=end

