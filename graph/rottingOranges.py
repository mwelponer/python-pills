from typing import List, Optional
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        qu = deque()        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    qu.append((r, c))

        if not fresh: return 0

        minutes = -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while qu:
            for i in range(len(qu)):
                r, c = qu.popleft()

                for dr, dc in dirs:
                    dr, dc = r + dr, c + dc

                    if dr in range(rows) and dc in range(cols) and grid[dr][dc] == 1:
                        fresh -= 1
                        grid[dr][dc] = 2
                        qu.append((dr, dc))
            minutes += 1

        return minutes if not fresh else -1


s = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]

print(s.orangesRotting(grid))
