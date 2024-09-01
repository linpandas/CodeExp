#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "]":"[", "}":"{"}
        for item in s:
            if item in dic.values():
                stack.append(item)
            elif not stack or dic[item] != stack[-1]:
                return False
            else:
                stack.pop()
        
        return not stack
# @lc code=end

