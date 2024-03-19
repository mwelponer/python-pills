#pragma once
#include "Utils.h"
#include <vector>

using namespace mike;

class Graphs {
public:
    int numIslands(std::vector<std::vector<char>>& grid);
    Node* cloneGraph(Node* node);
};