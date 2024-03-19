from typing import Optional
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    map = {}
    for i, n in enumerate(nums):
        if (target - n) in map:
            return [map[target - n], i]
        map[n] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
