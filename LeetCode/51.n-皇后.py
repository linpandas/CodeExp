#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = ["."*n for _ in range(n)]
        result = []
        self.backtracking(n, 0, chessboard, result)
        return result

    def backtracking(self, n, row, chessboard, result):
        if row == n:
            result.append(chessboard.copy())
            return

        for col in range(n):
            if self.isValid(chessboard, row, col):
                chessboard[row] = chessboard[row][:col] + "Q" + chessboard[row][col+1:]
                self.backtracking(n, row+1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + "." + chessboard[row][col+1:]

    def isValid(self, chessboard, row, col):
        # 检查列
        for i in range(row):
            if chessboard[i][col] == "Q":
                return False

        # 检查45度角
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # 检查135度角
        i, j = row-1, col+1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True
# @lc code=end

