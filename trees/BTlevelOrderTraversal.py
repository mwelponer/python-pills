from typing import Optional
import sys, os

# setting path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_dir)
from utils import TreeNode
from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        qu = deque([root])

        while qu:
            level = []
            for i in range(len(qu)):
                node = qu.popleft()
                if node:
                    level.append(node.val)
                    if node.left: qu.append(node.left)
                    if node.right: qu.append(node.right)
            if level:
                res.append(level)

        return res


s = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.levelOrder(root))
