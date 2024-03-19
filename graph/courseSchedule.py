from typing import List, Optional
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjmap = defaultdict(list)
        for cou, pre in prerequisites:
            adjmap[cou].append(pre)

        def dfs(course):
            if course in visit:
                return False
            if adjmap[course] == []:
                return True

            visit.add(course)
            for pre in adjmap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            adjmap[course] = []
            return True

        visit = set()
        for i in range(numCourses):
            if not dfs(i): return False

        return True

s = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(s.canFinish(numCourses, prerequisites))
