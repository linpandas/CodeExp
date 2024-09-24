#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, [], result)
        return result

    def backtracking(self, candidates, target, startIndex, path, result):
        if sum(path) > target:
            return
        if sum(path) == target:
            result.append(path.copy())
        for i in range(startIndex, len(candidates)):
            if sum(path) + candidates[i] > target:
                continue
            path.append(candidates[i])
            self.backtracking(candidates, target, i, path, result)
            path.pop()
# @lc code=end

