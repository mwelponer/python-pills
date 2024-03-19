from typing import Optional


def isHappy(n: int) -> bool:

    def squareDigitsSum(n):
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n = n // 10
        return sum


    slow, fast = n, squareDigitsSum(n)
    while slow != fast:
        slow = squareDigitsSum(slow)
        fast = squareDigitsSum(squareDigitsSum(fast))

    if slow == 1:
        return True

    return False


print(isHappy(69))
