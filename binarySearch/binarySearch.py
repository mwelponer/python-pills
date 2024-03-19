from typing import List


def search(nums: List[int], target: int) -> int:
    L, R = 0, len(nums) - 1

    while L <= R:
        mid = L + (R - L) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            R = mid - 1
        else:
            L = mid + 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))
