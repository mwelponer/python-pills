#include "HeapPriorityQueue.h"
#include "Utils.h"
#include "KthLargest.h"

int HeapPriorityQueue::lastStoneWeight(std::vector<int>& stones){
    //std::priority_queue<int> pq(stones.begin(), stones.end()); // perform in O(nlogn)
    std::priority_queue<int> pq(std::less<int>(), stones); // perform in O(n)

    while(pq.size() > 1){
        int x = pq.top(); 
        pq.pop();
        int y = pq.top(); 
        pq.pop();
        if (x != y)
            pq.push(std::abs(x - y));
    }

    return !pq.empty() ? pq.top() : 0;
}

std::vector<std::vector<int>> HeapPriorityQueue::kClosest(std::vector<std::vector<int>>& points, int k){
    typedef std::vector<int> pnt;
    
    ////////// priority queue version
    std::priority_queue<std::pair<float, int>> pq;
    for ( int i = 0; i < points.size(); i++ ){
        pnt p = points[i];
        pq.push({p[0]*p[0] + p[1]*p[1], i});
        if (pq.size() > k)
            pq.pop();
    }
    std::vector<pnt> res;
    while(!pq.empty()){
        res.push_back(points[pq.top().second]);
        pq.pop();
    }
    return res;

    ////////// nth_element() version
    // lambda function
    // auto func = [](pnt& a, pnt& b){
    //     return a[0]*a[0] + a[1]*a[1] < b[0]*b[0] + b[1]*b[1];
    // };

    // // order the first k elements according to func
    // std::nth_element(points.begin(), points.begin() + k, points.end(), func);
    // return std::vector<pnt>(points.begin(), points.begin() + k);
}

int main(){
    std::vector<int> nums;


    /* 1. Design a class to find the kth largest element in a stream. Note that it 
    is the kth largest element in the sorted order, not the kth distinct element.
    
    Implement KthLargest class:

    - KthLargest(int k, int[] nums) Initializes the object with the integer k and 
    the stream of integers nums.
    - int add(int val) Appends the integer val to the stream and returns the 
    element representing the kth largest element in the stream.*/
    std::cout << "\nKth Largest Element in a Stream" << std::endl;
    nums = {4, 5, 8, 2};
    KthLargest kl(3, nums);
    std::cout << kl.add(3) << std::endl;
    std::cout << kl.add(5) << std::endl;
    std::cout << kl.add(10) << std::endl;
    std::cout << kl.add(9) << std::endl;
    std::cout << kl.add(4) << std::endl;

    HeapPriorityQueue hpq;

    /* 2. You are given an array of integers stones where stones[i] is the weight of 
    the ith stone.
    We are playing a game with the stones. On each turn, we choose the heaviest two 
    stones and smash them together. Suppose the heaviest two stones have weights x 
    and y with x <= y. The result of this smash is:

    - If x == y, both stones are destroyed, and
    - If x != y, the stone of weight x is destroyed, and the stone of weight y has 
    new weight y - x.
    At the end of the game, there is at most one stone left.

    Return the weight of the last remaining stone. If there are no stones left, 
    return 0.*/
    std::cout << "\nLast Stone Weight" << std::endl;
    nums = {2,7,4,1,8,1}; mike::printVector(nums);
    std::cout << hpq.lastStoneWeight(nums) << std::endl;

    /* 3. Given an array of points where points[i] = [xi, yi] represents a 
    point on the X-Y plane and an integer k, return the k closest points to 
    the origin (0, 0).
    The distance between two points on the X-Y plane is the Euclidean distance 
    (i.e., √(x1 - x2)2 + (y1 - y2)2).
    You may return the answer in any order. The answer is guaranteed to be 
    unique (except for the order that it is in).
    */
    std::cout << "\nK Closest Points to Origin" << std::endl;
    std::vector<std::vector<int>> points = {{3, 3}, {5, -1}, {-2, 4}}; int k = 2;
    mike::printVec2d(points);
    mike::printVec2d(hpq.kClosest(points, k));

    std::pair<std::string, double> PAIR3; 
    PAIR3 = std::make_pair("GeeksForGeeks is Best", 4.56);
    PAIR3 = {"Mike is the Best", 4.56};
    std::cout << "first: " << PAIR3.first << ", second: " << PAIR3.second << std::endl;
}