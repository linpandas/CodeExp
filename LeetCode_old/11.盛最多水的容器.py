#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxV = min(height[l], height[r]) * (r-l)
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            maxV = max(maxV, min(height[l], height[r]) * (r-l))
        
        return maxV
# @lc code=end

