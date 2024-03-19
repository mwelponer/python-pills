from typing import List
from typing import Optional


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    size = len(nums)

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]: # to avoid duplicates
            continue

        l, r = i + 1, size - 1
        while l < r:
            sum = n + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else: # we found a good trisome :P
                res.append([n, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]: # avoid duplicates
                    l += 1

    return res


print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0,0]))
