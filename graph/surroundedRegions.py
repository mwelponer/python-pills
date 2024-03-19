from typing import Optional
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                board[r][c] != "O"): return

            board[r][c] = "U"

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        # starting from borders,
        # mark with "U" unsurrounded regions, using dfs
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r not in range(1, rows - 1) or
                    c not in range(1, cols - 1)):
                        dfs(r, c)

        # now everythng that is O is surrounded so we can flip to X
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # unmark "U" unsurrounded regions back to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "U":
                    board[r][c] = "O"

s = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(board)

s.solve(board)
print(board)
