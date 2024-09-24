#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        for i, num in enumerate(nums):
            if i <= cover:
                cover = max(cover, i + num)
                if cover >= len(nums)-1:
                    return True
        
        return False
# @lc code=end

