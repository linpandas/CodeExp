#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # 单调栈，存放下标
        result = [0] * len(temperatures)
        for i, item in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < item:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return result

# @lc code=end

