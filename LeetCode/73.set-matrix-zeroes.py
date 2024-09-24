#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rowSet, colSet = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # 标记
                    rowSet.add(i)
                    colSet.add(j)
            # 行置零
            if i in rowSet:
                matrix[i] = [0] * n
        # 列置零
        for j in colSet:
            for i in range(m):
                matrix[i][j] = 0
# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

