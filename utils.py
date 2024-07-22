from collections import deque
import heapq


"""
maxheap implementation
"""
class MaxHeap:
    def __init__(self, values=0):
        self.values = [-i for i in values]
        heapq.heapify(self.values)

    def heappop(self):
        return -1 * heapq.heappop(self.values)

    def heappush(self, val):
        heapq.heappush(self.values, -1 * val)

    def peek(self):
        return -1 * self.values[0]


"""
node of a graph
"""
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    """
    print out the entire graph starting from node self
    """
    def __str__(self):
        visited = {}

        def dfs(node):
            if node.val in visited: 
                return

            visited[node.val] = node
            for nei in node.neighbors:
                dfs(nei)
        
        dfs(self)
        if len(visited) <= 1: return "[[]]"

        s = "["
        for node in visited.values():
            s += "["
            for nei in node.neighbors:
                s += f"{nei.val}, "
            s = s[:-2] + "], "

        return s[:-2] + "]"


"""
build the graph from an adjacency list (optimized)
"""
def buildGraph(adjlist: 'List[List[int]]') -> 'Node':
    if not adjlist: # if graph has no nodes
        return None

    map = {} # maps 1-index:node

    def createNode(index):
        # if node is already in the map return it
        if index in map: # nodes are 1-indexed
            return map[index]

        # if node is not in the map create it and add it to the map
        newNode = Node(index)
        map[index] = newNode

        # add all node's neighbors according to the given adjacency list
        for i in adjlist[index-1]:
            nei = createNode(i) # createNode returns the node if already in map
            newNode.neighbors.append(nei) # add neighbor
            map[i] = nei # insert neighbor in the map

        return newNode

    createNode(1) # set 1 as the value of the first node

    return map[1]


"""
node of a singly linked list
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = "["
        while self:
            s += f"{self.val}, "
            self = self.next
        return s[:-2] + "]"


"""
node of a binary tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        queue = deque()
        queue.append(self)

        s = "["
        while queue:
            n = queue.popleft()
            s += f"{n.val}, "
            if n.left: queue.append(n.left)
            if n.right: queue.append(n.right)
        return s[:-2] + "]"


class DirectedGraph:
    class Node:
        def __init__(self, val=0, neighbors=None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []

        def __str__(self):
            visited = {}
            
            def dfs(node):
                if node.val in visited:
                    return
                visited[node.val] = node
                for nei in node.neighbors:
                    dfs(nei)
            
            dfs(self)
            if len(visited) <= 1: return "[[]]"

            s = "["
            for node in visited.values():
                s += "["
                for nei in node.neighbors:
                    s += f"{nei.val}, "
                s = s[:-2] + "], "
            return s[:-2] + "]"


    def __init__(self):
        self.nodes = {}

    def add_node(self, val):
        if val not in self.nodes:
            self.nodes[val] = Node(val)

    def add_edge(self, from_val, to_val):
        if from_val not in self.nodes:
            self.add_node(from_val)
        if to_val not in self.nodes:
            self.add_node(to_val)
        self.nodes[from_val].neighbors.append(self.nodes[to_val])

    def __str__(self):
        s = "["
        for node in self.nodes.values():
            s += f"{node.val}: ["
            for nei in node.neighbors:
                s += f"{nei.val}, "
            s = s[:-2] + "], "
        return s[:-2] + "]"

# DirectedGraph Example usage
graph = DirectedGraph()
graph.add_node(1)
graph.add_node(2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

print("Graph:")
print(graph)


# # Example usage Graph Node
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)

# node1.neighbors = [node2, node3]
# node2.neighbors = [node1]
# node3.neighbors = [node1]
# print(node1)

# # or simply 
# node = buildGraph([[2, 3], [1], [1]])
# print(node)