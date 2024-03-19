#include "SlidingWindow.h"
#include <iostream>

int SlidingWindow::maxProfit(std::vector<int>& prices) {
    int l = 0, r = 1;
    int profit = 0, max_pr = 0;
    
    while (r < prices.size()) {
        if (prices[l] < prices[r])
            profit = prices[r] - prices[l];
        else
            l = r;
        r++;
        
        max_pr = std::max(max_pr, profit);
    }
    
    return max_pr;
}

int main() {
    SlidingWindow sw;

    /* 1. You are given an array prices where prices[i] is the price of a given 
    stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock 
    and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you 
    cannot achieve any profit, return 0.
    */
    std::vector<int> prices = {7,1,5,3,6,4};
    std::cout << "\nBest Time to Buy And Sell Stock" << std::endl;
    std::cout << sw.maxProfit(prices) << std::endl;

}