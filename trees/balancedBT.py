from typing import Optional
import sys

# setting path
sys.path.append('../neetcode')
from utils import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # base case root is null
            if not root:
                return [-1, True]

            # recursively on left and right
            left = dfs(root.left)
            right = dfs(root.right)

            # once we recursively ended up to the simplest case we also
            # evaluate at the same time if it is balanced.
            # Conditions for a node to be balanced:
            # - height of left subt and height of right subt do not differ
            # more then 1
            # - left subt is balanced and right subt is balanced
            balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1

            # and we return height of the simple node and balanced boolean
            return [1 + max(left[0], right[0]), balanced]


        return dfs(root)[1]


s = Solution()

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.isBalanced(root))
root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)),
    TreeNode(3)), TreeNode(2))
print(s.isBalanced(root))
