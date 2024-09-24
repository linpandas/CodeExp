#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 0
        nums = set(nums)
        for num in nums:
            n = num
            count = 1
            if n - 1 not in nums:
                while n + 1 in nums:
                    count += 1
                    n += 1
                maxL = max(maxL, count)
        
        return maxL
# @lc code=end

