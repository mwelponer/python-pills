from typing import List, Optional

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # for each node let's keep track of the anchestor (parent)
        # and the rank of the connected component. At the beginning every
        # single node is the anchestor of itself. The rank of each node is 1
        # as there are no connections and each node is a connected component
        # made of exactly 1 node.
        parent = [ i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        # for each given edge let's try to make the connections calling union

        # used by union to find the anchestor of a node
        def find(n):
            p = parent[n]
            # we could have a path longer than 2
            while p != parent[p]:
                # a trick to get to the anchestor faster (path compression)
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a, b):
            # find the anchestor of both nodes
            pa, pb = find(a), find(b)

            # if nodes have the same anchestor,
            # this is the first connection that forms the cycle!
            if pa == pb:
                return False

            # if anchestors are different, let's connect the two components
            # how? anchestor with the higher rank becomes the parent of the other
            if rank[pa] >= rank[pb]:
                parent[pb] = pa
                rank[pa] += 1
            else:
                parent[pa] = pb
                rank[pb] += 1
            return True

        # now for each given edge let's try to make the connections
        for a, b in edges:
            if not union(a, b):
                return [a, b]

s = Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(s.findRedundantConnection(edges))
