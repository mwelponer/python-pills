#include "Graphs.h"
#include <iostream>

int rows, cols;
typedef std::vector<std::vector<char>> grid;

void numIslands_dfs(grid& grid, int r, int c){
    grid[r][c] = '0';
    
    if (r > 0 && grid[r-1][c] == '1')
        numIslands_dfs(grid, r-1, c);
    if (r < rows-1 && grid[r+1][c] == '1')
        numIslands_dfs(grid, r+1, c);
    if (c > 0 && grid[r][c-1] == '1')
        numIslands_dfs(grid, r, c-1);
    if (c < cols-1 && grid[r][c+1] == '1')
        numIslands_dfs(grid, r, c+1);
}

int Graphs::numIslands(grid& grid) {
    int res = 0;
    rows = grid.size(); cols = grid[0].size();

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (grid[r][c] == '1'){
                res++;
                numIslands_dfs(grid, r, c);
            }

    return res;
}

Node* cloneGraph_dfs(Node* node) {
    static std::unordered_map<Node*, Node*> oldToNew;

    if (oldToNew.count(node))
        return oldToNew[node];
    
    Node* cloned = new Node(node->val);
    oldToNew[node] = cloned;
    
    for (Node* nei : node->neighbors)
        cloned->neighbors.push_back(cloneGraph_dfs(nei));
    
    return cloned;
}

Node* Graphs::cloneGraph(Node* node) {
    return node ? cloneGraph_dfs(node) : NULL;
}

int main() {
    Graphs gr;
    
    /* 1. Given an m x n 2D binary grid grid which represents a map of '1's 
    (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands 
    horizontally or vertically. You may assume all four edges of the grid are 
    all surrounded by water.
    */
    grid grid = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'} };
    std::cout << "\nNumber of Islands" << std::endl;
    std::cout << gr.numIslands(grid) << std::endl;

    /* 2. Given a reference of a node in a connected undirected graph.
    Return a deep copy (clone) of the graph.
    Each node in the graph contains a value (int) and a list (List[Node]) of 
    its neighbors.

    class Node {
        public int val;
        public List<Node> neighbors;
    }
 
    Test case format:
    For simplicity, each node's value is the same as the node's index 
    (1-indexed). For example, the first node with val == 1, the second node 
    with val == 2, and so on. The graph is represented in the test case using 
    an adjacency list.
    An adjacency list is a collection of unordered lists used to represent a 
    finite graph. Each list describes the set of neighbors of a node in the 
    graph.
    The given node will always be the first node with val = 1. You must return 
    the copy of the given node as a reference to the cloned graph.
    */
    std::cout << "\nClone Graph" << std::endl;

    std::vector<std::vector<int>> adjList = {{2,4},{1,3},{2,4},{1,3}};
    Node* g = buildGraph(adjList);
    if (g) {
        g->print();
        Node* gclone = gr.cloneGraph(g);
        gclone->print();
        delete g;
        delete gclone;
    }

    // adjList = {{}};
    // g = buildGraph(adjList);
    // if (g) {
    //     g->print();
    //     Node* gclone = gr.cloneGraph(g);
    //     gclone->print();
    //     delete g;
    //     delete gclone;
    // }

    // adjList = {};
    // g = buildGraph(adjList);
    // if (g) {
    //     g->print();
    //     Node* gclone = gr.cloneGraph(g);
    //     gclone->print();
    //     delete g;
    //     delete gclone;
    // }
}