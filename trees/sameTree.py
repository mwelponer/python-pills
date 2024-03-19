from typing import Optional
import sys

# setting path
sys.path.append('../neetcode')
from utils import TreeNode


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    if not p and not q:
        return True

    if not q or not p:
        return False

    return (p.val == q.val and isSameTree(p.left, q.left)
        and isSameTree(p.right, q.right))


p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p, q))


p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(3))
print(isSameTree(p, q))
