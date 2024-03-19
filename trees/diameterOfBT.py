from typing import Optional
import sys

# setting path
sys.path.append('../neetcode')
from utils import TreeNode


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def recursive(root):
            if not root: # height of a null node is -1
                return -1

            leftH = recursive(root.left)
            rightH = recursive(root.right)
            diameter = leftH + rightH + 1 + 1 # evaluate diameter
            self.res = max(self.res, diameter) # update res variable

            # each time I recursively go down height is
            # 1 + the max height between left and right
            return 1 + max(leftH, rightH)

        recursive(root)
        return self.res


s = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(s.diameterOfBinaryTree(root))
