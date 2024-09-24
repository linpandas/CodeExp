#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        temp = [0] * len(s)
        stack = []
        curL, maxL = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()
                    if s[j] == "(":
                        temp[i], temp[j] = 1, 1
        
        for num in temp:
            if num:
                curL += 1
            else:
                maxL = max(maxL, curL)
                curL = 0
        maxL = max(curL, maxL)
        return maxL

# @lc code=end

