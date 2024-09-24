#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # 单调递增栈，存放数组下标
        result = 0
        for r, rh in enumerate(height):
            while stack and height[stack[-1]] < rh:
                mid = stack.pop()
                if stack:
                    l = stack[-1]
                    w = r - l - 1
                    h = min(height[l], height[r]) - height[mid]
                    result += w * h
            stack.append(r)
        
        return result
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

