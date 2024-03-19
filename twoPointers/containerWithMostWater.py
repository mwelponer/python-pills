from typing import Optional
from typing import List


def maxArea(height: List[int]) -> int:
    l, r, maximum = 0, len(height) - 1, 0

    while l < r:
        water = (r - l) * min(height[l], height[r])
        maximum = max(maximum, water)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return maximum


print(maxArea([1,8,6,2,5,4,8,3,7]))
