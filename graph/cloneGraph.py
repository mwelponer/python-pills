from typing import Optional
import sys, os

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
#print('parent_dir: ' + str(parent_dir))
# setting path
sys.path.append(parent_dir)
from utils import Node, buildGraph


def cloneGraph(node: 'Node') -> 'Node':

    oldToNew = {} # hashmap original : cloned

    def cloneDFS(node):
        if node in oldToNew: # if original in map return cloned
            return oldToNew[node]

        cloned = Node(node.val) # else clone original
        oldToNew[node] = cloned # put it into the hm

        for nei in node.neighbors: # create cloned connections with nei
            cloned.neighbors.append(cloneDFS(nei)) # recursively

        return cloned

    return cloneDFS(node) if node else None # run DFS


node = buildGraph([[2,4],[1,3],[2,4],[1,3]])
if node:
    print(node)
    print(cloneGraph(node))

node = buildGraph([[]])
if node:
    print(node)
    print(cloneGraph(node))

node = buildGraph([])
if node:
    print(node)
    print(cloneGraph(node))
