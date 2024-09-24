#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30204
#
# [240] 搜索二维矩阵 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False
        
# @lc code=end



#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#

