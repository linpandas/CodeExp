#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        
        return max(dp)
    
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # 贪心算法
#         result, cover = float("-inf"), 0
#         for i, num in enumerate(nums):
#             cover += num
#             if cover > result:
#                 result = cover
#             if cover < 0:
#                 cover = 0

#         return result
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

