#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        cur_d, next_d = 0, 0
        for i in range(len(nums)-1):
            next_d = max(next_d, i+nums[i])
            if i == cur_d:
                cur_d = next_d
                result += 1
        
        return result
# @lc code=end

