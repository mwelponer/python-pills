from typing import List
from typing import Optional
from collections import deque


def numIslands(grid: List[List[str]], visit: str) -> int:

    visited = set()
    rows, cols = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    res = 0

    def dfs(r, c):
        if (r not in range(rows) or c not in range(cols)
            or grid[r][c] == "0" or (r, c) in visited):
            return

        visited.add((r, c))

        dfs(r, c + 1)
        dfs(r, c - 1)
        dfs(r + 1, c)
        dfs(r - 1, c)

    def bfs(r, c):
        qu = deque([(r, c)])
        visited.add((r, c))

        while qu:
            for i in range(len(qu)):
                row, col = qu.popleft()

                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c) not in visited):
                        qu.append((r, c))
                        visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                if visit == "dfs":
                    dfs(r, c)
                elif visit == "bfs":
                    bfs(r, c)
                else:
                    raise NameError('Visiting can be "dfs" or "bfs"')
                res += 1

    return res


# grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"] ]
# print(numIslands(grid))


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"] ]
print(numIslands(grid, "dfs"))
print(numIslands(grid, "bfs"))
