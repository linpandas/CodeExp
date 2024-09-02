#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和
        from collections import defaultdict
        preSum = defaultdict(int)
        preSum[0] = 1
        curSum, result = 0, 0
        for num in nums:
            curSum += num
            # 如果curSum - k不在preSum中，则加0
            result += preSum[curSum - k]
            preSum[curSum] += 1
        
        return result
# @lc code=end

