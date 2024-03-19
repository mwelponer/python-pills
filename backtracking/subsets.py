from typing import Optional
from typing import List

#                          [1,2,3]
#                [1]                     []
#      [1,2]            [1]         [2]       []
# [1,2,3] [1,2]     [1,3] [1]   [2,3] [2]  [3]   []

def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    subset = []
    def dfs(index):
        if index >= len(nums):
            res.append(subset.copy())
            return

        # include nums[index]
        subset.append(nums[index])
        dfs(index + 1)

        # not include nums[index]
        subset.pop() # remove last inserted
        dfs(index + 1)

    dfs(0)
    return res


print(subsets([1, 2, 3]))
