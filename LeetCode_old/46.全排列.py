#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, [False]*len(nums), [], result)
        return result

    def backtracking(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, used, path, result)
            used[i] = False
            path.pop()
# @lc code=end

