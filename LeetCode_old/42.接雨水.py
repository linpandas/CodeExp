#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        for r, rh in enumerate(height):
            while stack and rh > height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    l = stack[-1]
                    w = r - l - 1
                    h = min(height[l], rh) - height[mid]
                    result += w * h
            stack.append(r)
        
        return result
# @lc code=end

