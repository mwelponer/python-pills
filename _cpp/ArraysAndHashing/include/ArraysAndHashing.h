#pragma once

#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>

class ArraysAndHashing {
public:
    bool containsDuplicate(std::vector<int>& nums);
    bool isAnagram(std::string s, std::string t);
    std::vector<int> twoSum(std::vector<int>& nums, int target);
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs);
    std::vector<int> topKFrequent(std::vector<int>& nums, int k);
};