#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        target = sum_ // 2
        # 容量为j的背包，所背的物品价值最大可以为dp[j]
        dp = [0] * (target+1)
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j-num]+num)
        if dp[target] == target:
            return True
        return False
# @lc code=end

