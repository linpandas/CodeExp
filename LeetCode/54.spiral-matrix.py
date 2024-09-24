#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n-1, 0, m-1
        result = []
        while True:
            for j in range(l, r+1):
                result.append(matrix[t][j])
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                result.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for j in range(r, l-1, -1):
                result.append(matrix[b][j])
            b -= 1
            if t > b:
                break
            for i in range(b, t-1, -1):
                result.append(matrix[i][l])
            l += 1
            if l > r:
                break
        
        return result
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

