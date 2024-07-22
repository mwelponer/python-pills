from typing import Optional
import sys, os
from collections import deque

# setting path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_dir)
from utils import TreeNode


def maxDepth_recursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth_recursive(root.left),
        maxDepth_recursive(root.right))


def maxDepth_BFS(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    level = 0
    qu = deque([root])
    while qu:

        for i in range(len(qu)): # enqueue all nodes on the same level
            node = qu.popleft()
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)

        level += 1 # increment the level variable

    return level


def maxDepth_DFS(root: Optional[TreeNode]) -> int:
    maxlevel = 0

    st = [[root, 1]] # initialize stack with tuple [node_root, level_1]
    while st:
        node, level = st.pop()

        if node:
            print(node.val)
            maxlevel = max(maxlevel, level)
            st.append([node.left, level + 1])
            st.append([node.right, level + 1])

    return maxlevel

#     3
# 9       20
#       15   7
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root.toString()

#        3
#    9       20
# 15   7
# root = TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))
# root.toString()

print(maxDepth_recursive(root)) # method using recursion
print(maxDepth_BFS(root)) # method using bread first search
print(maxDepth_DFS(root)) # method using depth first search

# root = TreeNode(1)
# print(maxDepth_recursive(root))
