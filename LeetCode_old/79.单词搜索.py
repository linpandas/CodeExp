#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False]*n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(x, y, k) -> bool:
            if board[x][y] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            used[x][y] = True
            for dx, dy in dirs:
                nextx = x + dx
                nexty = y + dy
                if 0 <= nextx < m and 0 <= nexty < n and not used[nextx][nexty]:
                    if dfs(nextx, nexty, k+1):
                        return True
            used[x][y] = False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
# @lc code=end

