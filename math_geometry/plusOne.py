from typing import List
from typing import Optional

def plusOne(digits: List[int]) -> List[int]:

    ptr = len(digits) - 1

    res = []
    reminder = 1
    while ptr >= 0 or reminder:
        sum = reminder
        if ptr >= 0:
            sum += digits[ptr]
        if sum > 9:
            res.append(0)
            reminder = 1
        else:
            res.append(sum)
            reminder = 0
        ptr -= 1

    res.reverse()
    return res



print(plusOne([1,2,3]))
