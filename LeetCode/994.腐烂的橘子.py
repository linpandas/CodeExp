#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = []
        fresh, result = 0, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue:
            result += 1
            temp = queue
            queue = []
            for x, y in temp:
                for dx, dy in dirs:
                    nextx = x + dx
                    nexty = y + dy
                    if 0 <= nextx < m and 0 <= nexty < n and grid[nextx][nexty] == 1:
                        fresh -= 1
                        grid[nextx][nexty] = 2
                        queue.append((nextx, nexty))
        
        return -1 if fresh else max(0, result)
# @lc code=end

