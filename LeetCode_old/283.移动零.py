#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r, num in enumerate(nums):
            if num != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
# @lc code=end

