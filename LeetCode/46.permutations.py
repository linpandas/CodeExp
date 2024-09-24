#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, [False]*len(nums), [], result)
        return result

    def backtracking(self, nums, used, path, result):
        if len(nums) == len(path):
            result.append(path.copy())
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, used, path, result)
            used[i] = False
            path.pop()
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

