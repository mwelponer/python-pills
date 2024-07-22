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


"""
implementation of a graph using adjacency list
"""
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


"""
implementation of a `Least recently used` cache
"""
class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key, self.val = key, val
            self.prev, self.next = None, None

    # an empty cache look like `head -> tail`,
    #where tail is the last added
    def __init__(self, capacity):
        self.capacity = capacity
        self.head, self.tail = self.Node(-1, 0), self.Node(-1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def __str__(self):
        s = 'head -> '
        n = self.head.next 
        while n:
            if n.key != -1:
                s += f'{n.key} -> '
            else:
                s += 'tail'
            n = n.next
        return s
    
    # adds a node just before the tail, making it 
    # the most recently used item.
    def add(self, node):
        print(f'  add node {node.key}')
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    # remove a specific node inside the linkedlist
    def remove(self, node):
        print(f'  remove {node.key}');
        pr = node.prev
        nx = node.next
        pr.next = nx
        nx.prev = pr

    # moves an existing node to just before the tail, 
    # marking it as the most recently used.
    def moveToTail(self, node):
        print(f'  move {node.key} to tail');
        self.remove(node)
        self.add(node)
  
    # retrieves the value associated with a key if it exists
    def get(self, key):
        print(f'\ngetting node {key} [')
        # get if present
        value = -1

        if key in self.map:
            # retrieve node
            toGet = self.map[key]
            value = toGet.val
            # move to tail (most recently inserted), to become most recently used
            self.moveToTail(toGet)
        
        print(f'  returns value {value}')
        print(f'] : {self}')
        return value
  
    # add to the cache
    # adds a new key-value pair to the cache. If the cache is full, 
    # it removes the least recently used item (the node right after head)
    def put(self, key, value):
        print(f'\nputting {key}:{value} [')
        # if key exists update node and move it to tail as most recently used
        if key in self.map:
            print(f'  updating node {key}')
            node = self.map[key]
            node.value = value
            self.moveToTail(node)
        else:
            toBeAdded = self.Node(key, value)

            if len(self.map) == self.capacity:
                print('  cache is full')
                # remove least recently used (head)
                toBeRemoved = self.head.next
                self.remove(toBeRemoved)
                self.map.pop(toBeRemoved.key)

            self.add(toBeAdded)
            self.map[key] = toBeAdded
        print(f'] : {self}')


# # Least recently used cache Example
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)        # returns 1
cache.put(3, 3)     # evicts key 2
cache.get(2)        # returns -1 (not found)
cache.put(4, 4)     # evicts key 1
cache.get(1)        # returns -1 (not found)
cache.get(3)        # returns 3
cache.get(4)        # returns 4


# # DirectedGraph Example
# graph = DirectedGraph()
# graph.add_node(1)
# graph.add_node(2)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(2, 3)
# graph.add_edge(3, 4)

# print("Graph:")
# print(graph)


# # Graph Node Example
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)

# node1.neighbors = [node2, node3]
# node2.neighbors = [node1]
# node3.neighbors = [node1]
# print(node1)

# # buildGraph function Example
# node = buildGraph([[2, 3], [1], [1]])
# print(node)