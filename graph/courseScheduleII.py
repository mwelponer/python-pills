from typing import List, Optional

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjmap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            adjmap[c].append(p)

        res = []

        def dfs(crs):
            # impossible: there is a cycle!
            if crs in visited:
                return False

            # if course has already been taken
            if crs in done:
                return True

            # track visited to intercept possible cycles
            visited.add(crs)
            for pre in adjmap[crs]: # for each prerequisites
                if not dfs(pre): #
                    return False
            print('removing course')
            visited.remove(crs)

            # al prerequisites are satisfied so
            # we can add course to done set
            # and to res solution too
            done.add(crs)
            res.append(crs)

            return True

        visited, done = set(), set()
        for crs in range(numCourses): # for every course
            print('course', crs)
            if not dfs(crs):
                return [] # return empty list if impossible

        return res

s = Solution()

# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# print(s.findOrder(numCourses, prerequisites))

numCourses = 6
prerequisites = [[5,0],[4,0],[0,1],[0,2],[1,3],[3,2]]
print(s.findOrder(numCourses, prerequisites))
