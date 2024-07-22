from typing import Optional
import sys, os
from collections import deque

# setting path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_dir)
from utils import TreeNode


class Solution:

    def BFS(self, root: TreeNode):
        level = 0
        qu = deque([root])

        while qu:
            printLevel = ""
            for i in range(len(qu)):
                node = qu.popleft()
                if node.left: qu.append(node.left)
                if node.right: qu.append(node.right)

                printLevel += (str(node.val) + ", ")

            if not qu: printLevel = printLevel[:-2] + "."
            print(printLevel)
            level += 1

    def DFS(self, root: TreeNode):
        st = [root]
        toPrint = "DSF stack: "
        while st:
            node = st.pop()
            if node.right: st.append(node.right)
            if node.left: st.append(node.left)

            toPrint += str(node.val) + ", "

        print(toPrint[:-2] + ".")


    def recursive(self, root: TreeNode):

        def preorder(root):
            if not root:
                return ""

            self.toPrint += str(root.val) + ", "
            preorder(root.left)
            preorder(root.right)

        def inorder(root):
            if not root:
                return ""

            inorder(root.left)
            self.toPrint += str(root.val) + ", "
            inorder(root.right)

        def postorder(root):
            if not root:
                return ""

            postorder(root.left)
            postorder(root.right)
            self.toPrint += str(root.val) + ", "

        self.toPrint = "DFS recursive pre-order: "
        preorder(root)
        print(self.toPrint[:-2] + ".")

        self.toPrint = "DFS recursive in-order: "
        inorder(root)
        print(self.toPrint[:-2] + ".")

        self.toPrint = "DFSrecursive post-order: "
        postorder(root)
        print(self.toPrint[:-2] + ".")

s = Solution()

#               3
#         4          5
#      1     2
#           0
# root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
# s.BFS(root)

#               1
#         2          3
#      4     5
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
s.DFS(root)
s.recursive(root)
