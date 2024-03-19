from typing import Optional
from typing import List


# def twoSum(numbers: List[int], target: int) -> List[int]:
    # l, r = 0, len(numbers) - 1
    #
    # while(l < r):
    #     if numbers[l] + numbers[r] == target:
    #         return [l + 1, r + 1]
    #     if numbers[l] + numbers[r] > target:
    #         r -= 1
    #     else:
    #         l += 1

def twoSum(numbers: List[int], target: int) -> List[int]:
    hm = {}

    for i, n in enumerate(numbers):
        if (target - n) in hm:
            return [hm[target - n] + 1, i + 1]
        hm[n] = i


print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))
