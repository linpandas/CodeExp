#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除自身以外数组的乘积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        k = 1
        for i in range(n):
            result[i] *= k
            k *= nums[i]
        k = 1
        for i in range(n-1, -1, -1):
            result[i] *= k
            k *= nums[i]

        return result
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

