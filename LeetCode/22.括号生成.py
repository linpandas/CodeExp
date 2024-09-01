#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(path, left, right):
            # left：左括号的剩余数量
            # right：右括号的剩余数量
            if left == 0 and right == 0:
                result.append(path)
            if right < left:
                return
            if left > 0:
                dfs(path+"(", left-1, right)
            if right > 0:
                dfs(path+")", left, right-1)
        dfs("", n, n)
        return result
# @lc code=end

