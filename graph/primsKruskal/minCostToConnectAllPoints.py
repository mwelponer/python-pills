from typing import Optional, List

class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # create edges and relative adjacency list
        adjlst = defaultdict(list)
        for i in range(N):
            for j in range(i + 1, N):
                xi, yi = points[i]
                xj, yj = points[j]
                d = abs(xi - xj) + abs(yi - yj)
                adjlst[i].append((j, d))
                adjlst[j].append((i, d))


        # Prim's algorithm
        visited = set() # we add starting node to the set
        frontier = [[0, 0]] # add (distance, node) to the minheap
        cost = 0
        while len(visited) < N:
            dist, p = heapq.heappop(frontier) # pop the closest point
            if p in visited: # skip already seen points
                continue
            cost += dist # update total min cost
            visited.add(p) # add point to visited

            # add neighboars to frontier
            for neighbor, dist in adjlst[p]:
                if neighbor not in visited:
                    heapq.heappush(frontier, [dist, neighbor])

        return cost
        

s = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

print(s.minCostConnectPoints(points))
