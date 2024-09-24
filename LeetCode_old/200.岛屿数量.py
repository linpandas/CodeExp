#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        result = 0

        def dfs(x, y):
            if visited[x][y] or grid[x][y] == "0":
                return
            visited[x][y] = True
            for dx, dy in dirs:
                nextx = x + dx
                nexty = y + dy
                if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:
                    continue
                dfs(nextx, nexty)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    result += 1
                    dfs(i, j)
        
        return result
        
# @lc code=end

