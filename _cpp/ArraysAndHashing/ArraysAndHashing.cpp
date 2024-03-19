#include "ArraysAndHashing.h"
#include "Utils.h"
#include <iostream>

int cmpV(std::pair<int, int> a, std::pair<int, int> b){
	return a.second > b.second;
}

bool ArraysAndHashing::containsDuplicate(std::vector<int>& nums){
    std::unordered_set<int> hset;

    for (int n : nums){
        if (hset.find(n) == hset.end())
            hset.insert(n);
        else
            return true;
    }

    return false;
}

bool ArraysAndHashing::isAnagram(std::string s, std::string t){
    if (s.length() != t.length())
        return false;

    std::vector<int> freq(26);

    for (size_t i=0; i < s.length(); i++){
        int val = int(s.at(i)) - int('a');
        freq[val]++;
        val = int(t.at(i)) - int('a');
        freq[val]--;
    }

    for (auto x : freq)
        //std::cout << x << std::endl;
        if(x != 0) return false;

    return true;
}

std::vector<int> ArraysAndHashing::twoSum(std::vector<int>& nums, int target){
    std::unordered_map<int, int> hm;
    for (int i=0; i < nums.size(); i++){
        int diff = target - nums[i];
        if (hm.count(diff) == 1)
            return {hm[diff], i};

        hm[nums[i]] = i; 
    }

    return {-1, -1};
}

std::vector<std::vector<std::string>> ArraysAndHashing::groupAnagrams(
    std::vector<std::string>& strs) {
    
    // map key(string): 26 letters count
    // value(vector of strings): anagrams list
    std::unordered_map< 
        std::string, 
        std::vector<std::string> > map;
    
    // cycle over all strings
    for (std::string str : strs){
        // fill a vector of 26 letters count
        std::vector<int> letter_count(26, 0); 
        for(char c : str)
            letter_count[int(c) - int('a')]++;
        
        // key is obtained doing vector to string
        std::string key;
        for(int l : letter_count)
            key.append(std::to_string(l) + '#');
        
        // add new anagram 
        map[key].push_back(str);
    }
    
    // vectorize all grouped anagram  
    std::vector<std::vector<std::string>> res;
    for (auto it = map.begin(); it != map.end(); it++)
        res.push_back(it->second);
    
    return res;
}

std::vector<int> ArraysAndHashing::topKFrequent(std::vector<int>& nums, int k) {
    // fill a map (key, frequency) O(n)
    std::unordered_map<int, int> map;
    for (int n : nums)
        map[n]++;
    
    /// O(nlogn) SOLUTION ///
//         // convert map in vector of pair O(n)
//         std::vector<pair<int, int>> vec(map.begin(), map.end());
//         // sort vector according to pair.second (map value) O(nlogn)
//         sort(vec.begin(), vec.end(), cmpV);
//         // extract first k elements O(k)
//         std::vector<int> res;
//         for (int i=0; i < k; i++)
//             res.push_back(vec[i].first);
    
    /// O(n) SOLUTION ///
    // bucket with list of values at specified frequency 
    std::vector<std::vector<int>> bucket(nums.size() + 1);
    
    // fill the bucket
    for (auto it = map.begin(); it != map.end(); it++)
        bucket[it->second].push_back(it->first);
    
    // fill res starting from most frequent values
    std::vector<int> res;
    for (int i = nums.size(); i >= 0; i--) {
        if (res.size() == k) break;
        
        // if there are values with i frequency
        if (!bucket[i].empty()) {
            for (int n : bucket[i]) {
                res.push_back(n);
                if (res.size() == k) break;
            }
        }
    }
        
    return res;
}


int main(){
    std::vector<int> nums;
    std::string s, t;

    ArraysAndHashing aa;

    /* 1. Given an integer array nums, return true if any value appears at least 
    twice in the array, and return false if every element is distinct. */
    std::cout << "\nContains Duplicate" << std::endl;

    nums = {1,1,1,3,3,4,3,2,4,2}; mike::printVector(nums);
    std::cout << aa.containsDuplicate(nums) << std::endl;

    /* 2. Given two strings s and t, return true if t is an anagram of s, and false 
    otherwise. An Anagram is a word or phrase formed by rearranging the letters 
    of a different word or phrase, typically using all the original letters 
    exactly once.
    */
    std::cout << "\nValid Anagram" << std::endl;

    s = "anagram", t = "nagaram"; std::cout << s << ", " << t << std::endl;
    std::cout << aa.isAnagram(s, t) << std::endl;    

    /* 3. Given an array of integers nums and an integer target, return indices of 
    the two numbers such that they add up to target. You may assume that each input 
    would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    */
    std::cout << "\nTwo Sum" << std::endl;

    nums = {2, 7, 11, 15}; mike::printVector(nums);
    mike::printVector(aa.twoSum(nums, 9));

    /* 4. Given an array of strings strs, group the anagrams together. 
    You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a 
    different word or phrase, typically using all the original letters exactly 
    once.
    */
    std::cout << "\nGroup Anagrams" << std::endl;

    std::vector<std::string> strs = {"eat","tea","tan","ate","nat","bat"};
    std::vector<std::vector<std::string>> res = aa.groupAnagrams(strs);
    for (auto group : res)
        mike::printVector(group);

    /* 5. Given an integer array nums and an integer k, return the k most 
    frequent elements. You may return the answer in any order.
    */
    std::cout << "\nTop K Frequent Elements" << std::endl;

    nums = {1,1,1,2,2,3};
    mike::printVector(aa.topKFrequent(nums, 2));
    nums = {1};
    mike::printVector(aa.topKFrequent(nums, 1));

    nums.shrink_to_fit();
    std::cout << nums.capacity() << std::endl;
}