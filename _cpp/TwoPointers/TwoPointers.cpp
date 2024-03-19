#include "TwoPointers.h"
#include <iostream>

bool TwoPointers::isPalindrome(std::string s){
    int l = 0; 
    int r = s.size() - 1;

    while ( l < r ) {
        while ( !isalnum(s.at(l)) && l < r) l++;
        while ( !isalnum(s.at(r)) && l < r) r--;
        //std::cout << s.at(l) << ":" << s.at(r) << std::endl;
        if (tolower(s.at(l)) != tolower(s.at(r)))
            return false;
        l++;r--;
    }
        
    return true;
}

int main() {
    std::string s;

    TwoPointers tp;

    /* 1. A phrase is a palindrome if, after converting all uppercase letters 
    into lowercase letters and removing all non-alphanumeric characters, it 
    reads the same forward and backward. Alphanumeric characters include 
    letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.*/
    std::cout << "\nValid Palindrome" << std::endl;    
    s = "A man, a plan, a canal: Panama";
    std::cout << tp.isPalindrome(s) << std::endl;
}