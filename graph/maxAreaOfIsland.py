from typing import List
from typing import Optional
from collections import deque


def maxAreaOfIslandDFS(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    vis = set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    maxarea = 0

    def dfs(r, c):
        if (r not in range(rows) or c not in range(cols)
                or (r, c) in vis or grid[r][c] == 0): return 0
        vis.add((r, c))
        area = 1
        for dr, dc in dirs:
            area += dfs(dr + r, dc + c)

        return area


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                maxarea = max(maxarea, dfs(r, c))

    return maxarea

def maxAreaOfIslandBFS(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    vis = set()
    maxarea = 0

    def bfs(r, c):
        area = 0
        qu = deque()
        qu.append((r, c))
        while qu:
            cell = qu.popleft()
            cr, cc = cell[0], cell[1]
            if (cr not in range(rows) or cc not in range(cols)
                or (cr, cc) in vis or grid[cr][cc] == 0): continue
            vis.add((cr, cc))
            area += 1
            for d in dirs:
                dr, dc = cr + d[0], cc + d[1]
                qu.append((dr, dc))
        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                maxarea = max(maxarea, bfs(r, c))

    return maxarea


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIslandDFS(grid))
print(maxAreaOfIslandBFS(grid))
