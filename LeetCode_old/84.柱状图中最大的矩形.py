#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈（与接雨水呼应）
        heights.insert(0, 0)
        heights.append(0)
        stack = [] # 单调栈，存放数组下标
        result = 0
        for r, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                mid = stack.pop()
                if stack:
                    l = stack[-1]
                    w = r - l - 1
                    h = heights[mid]
                    result = max(result, w*h)
            stack.append(r)
        return result
# @lc code=end

