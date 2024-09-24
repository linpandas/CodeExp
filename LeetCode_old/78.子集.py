#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, 0, [], result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        result.append(path.copy())
        # if startIndex >= len(nums):
        #     # 终止条件可以不写，因为当startIndex >= len(nums)时
        #     # 下面的for循环不会执行
        #     return
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()
# @lc code=end

