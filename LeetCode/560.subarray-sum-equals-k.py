#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        preSum = defaultdict(int)
        preSum[0] = 1
        curSum, result = 0, 0
        for num in nums:
            curSum += num
            if curSum - k in preSum:
                result += preSum[curSum - k]
            preSum[curSum] += 1
        
        return result
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

