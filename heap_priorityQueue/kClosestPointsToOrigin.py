from typing import List
from typing import Optional
from collections import defaultdict
import math, heapq


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    ddict = defaultdict(list)

    for p in points:
        dist = math.sqrt(p[0] ** 2 + p[1] ** 2)
        ddict[dist].append(p)
        heapq.heappush(heap, dist)

    res = []
    while len(res) < k:
        dist = heapq.heappop(heap)
        points = ddict[dist]
        for p in points:
            res.append(p)
            if len(res) == k:
                break

    return res


print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))
