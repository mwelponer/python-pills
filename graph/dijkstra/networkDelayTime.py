from typing import Optional, List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times : List[List[int]], n : int, k : int) -> int :

        # transform edges list into an adjacency list
        adjMap = defaultdict(list) # node:list of adjacent nodes
        for e, v, w in times: # e = edge, v = vertex, w = weight (i.e. the time)
            adjMap[e].append((v, w)) # for each vertex, a list of neighbours with relative weight


        # Dijkstra algorithm
        res = 0
        minHeap = [(0, k)] # priority queue (time, node) ordered by time, initialized with starting node k
        visit = set() # to intercept cycles

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = max(res, time)

            # BFS on adjacent nodes
            for v, w in adjMap[node]:
                totTime = time + w
                heapq.heappush(minHeap, (totTime, v))

        return res if len(visit) == n else -1


times = [[2,1,1], [2,3,1], [3,4,1]]
s = Solution()

print(s.networkDelayTime(times, 4, 2))
