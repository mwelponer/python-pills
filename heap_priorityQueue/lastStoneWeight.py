from typing import Optional
from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-i for i in stones]
    heapq.heapify(stones) # O(N)

    while len(stones) > 1:
        res = abs(heapq.heappop(stones) * -1
            - heapq.heappop(stones) * -1) # 2 * O(lgN)
        if res != 0:
            heapq.heappush(stones, -res)

    return -stones[0] if len(stones) > 0 else 0


print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1]))
