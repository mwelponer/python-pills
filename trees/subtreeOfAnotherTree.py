from typing import Optional
import sys

# setting path
sys.path.append('../neetcode')
from utils import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sametree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                sametree(t1.left, t2.left) and
                sametree(t1.right, t2.right))

        if not subRoot: # (or not root and not subRoot)
            return True
        if not root:
            return False
        if sametree(root, subRoot):
            return True

        # if root and subRoot
        return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))


s = Solution()

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(s.isSubtree(root, subRoot))

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(s.isSubtree(root, subRoot))
