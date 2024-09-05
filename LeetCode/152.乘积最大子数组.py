#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        pre_min, pre_max = nums[0], nums[0]
        for num in nums[1:]:
            cur_min = min(pre_min*num, pre_max*num, num)
            cur_max = max(pre_min*num, pre_max*num, num)
            result = max(result, cur_max)
            pre_min = cur_min
            pre_max = cur_max
        return result
# @lc code=end

