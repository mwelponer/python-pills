from typing import List


def maxProfit(prices: List[int]) -> int:
    res = 0
    l = 0

    for r in range(1, len(prices)):
        if prices[l] > prices[r]:
            l = r
        res = max(res, prices[r] - prices[l])

    return res

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

prices = [7,2,5,1,6,4]
print(maxProfit(prices))
