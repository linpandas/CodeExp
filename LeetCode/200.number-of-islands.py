#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start

# @lcpr-template-end
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
                if 0 <= nextx < m and 0 <= nexty < n:
                    dfs(nextx, nexty)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    result += 1
                    dfs(i, j)
        
        return result

# class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     # bfs
    #     from collections import deque
    #     m, n = len(grid), len(grid[0])
    #     visited = [[False]*n for _ in range(m)]
    #     dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    #     result = 0

    #     def bfs(x, y):
    #         queue = deque([(x, y)])
    #         visited[x][y] = True
    #         while queue:
    #             x, y = queue.popleft()
    #             for dx, dy in dirs:
    #                 nextx, nexty = x+dx, y+dy
    #                 if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:
    #                     continue
    #                 if not visited[nextx][nexty] and grid[nextx][nexty] == "1":
    #                     queue.append((nextx, nexty))
    #                     visited[nextx][nexty] = True
        
    #     for i in range(m):
    #         for j in range(n):
    #             if not visited[i][j] and grid[i][j] == "1":
    #                 result += 1
    #                 bfs(i, j)
        
    #     return result
# @lc code=end



#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#

