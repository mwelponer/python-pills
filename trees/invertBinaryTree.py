from typing import Optional
import sys

# setting path
sys.path.append('../neetcode')
from utils import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    # swap left and right
    temp = root.left
    root.left = root.right
    root.right = temp

    # apply it recursively
    invertTree(root.left)
    invertTree(root.right)

    return root


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(7, TreeNode(6), TreeNode(9)))
root.toString()

invertTree(root).toString()
