from typing import Optional
from typing import List
from collections import defaultdict

def isValidSudoku(board: List[List[str]]) -> bool:
    size = len(board)

    # check each row
    for r in range(size):
        hset = set()
        for c in range(size):
            val = board[r][c]
            if val == '.': continue
            if val in hset:
                return False
            hset.add(c)

    # check each column
    for c in range(size):
        hset = set()
        for r in range(size):
            val = board[r][c]
            if val == '.': continue
            if val in hset:
                return False
            hset.add(val)

    # an hashmap of all hashsets, one set for each 3x3 subsquare
    # key: subsquare coords, value: hashset
    setsMap = defaultdict(set)
    for r in range(size):
        for c in range(size):
            val = board[r][c]
            if val == '.': continue
            if val in setsMap[(r//3, c//3)]: # subsquare hset contains val!
                return False
            setsMap[(r//3, c//3)].add(val) # add val to the subsquare hset

    return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
