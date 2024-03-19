#include "BinarySearch.h"
#include "Utils.h"
#include <iostream>

int BinarySearch::search(std::vector<int>& nums, int target){
    int left = 0, right = nums.size() - 1;

    while( left <= right){
        int pivot = left + (right - left) / 2;
        if (nums[pivot] == target)
            return pivot;
        else if(nums[pivot] > target)
            right = pivot - 1;
        else
            left = pivot + 1;
    }

    return -1;
}

int main(){
    std::vector<int> nums;
    std::string s, t;

    BinarySearch bs;

    /* 1. Given an array of integers nums which is sorted in ascending order, and 
    an integer target, write a function to search target in nums. If target 
    exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.
    */
    std::cout << "\nSearch" << std::endl;

    nums = {-1,0,3,5,9,12}; int target = 9; mike::printVector(nums);
    std::cout << bs.search(nums, target) << std::endl;
}