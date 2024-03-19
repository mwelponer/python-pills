#pragma once
#include <vector>
#include <queue>
#include <iostream>

class HeapPriorityQueue{
public:
    int lastStoneWeight(std::vector<int>& stones);
    std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int k);
};