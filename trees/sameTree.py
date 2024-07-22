from typing import Optional
import sys, os

# setting path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_dir)
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
