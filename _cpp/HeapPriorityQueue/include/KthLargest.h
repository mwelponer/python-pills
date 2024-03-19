#pragma once

#include <vector>
#include <queue>

class KthLargest {
private:
    int m_k;
    std::priority_queue<int> pq;

public:
    KthLargest (int k, std::vector<int>& nums)
        : m_k(k) {
        for (auto n : nums)
            pq.push(-n); // minheap
            if (pq.size() > m_k)
                pq.pop();
    }

    int add(int val){
        pq.push(-val);

        while (pq.size() > m_k)
            pq.pop();

        return -pq.top();
    }
};