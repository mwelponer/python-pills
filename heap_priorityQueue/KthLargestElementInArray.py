from typing import Optional
from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heapq.heapify(nums) # O(N)

    for i in range(len(nums) - k):
        heapq.heappop(nums) # O(lgN)

    return heapq.heappop(nums)


print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
