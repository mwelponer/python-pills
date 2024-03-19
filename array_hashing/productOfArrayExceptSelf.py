from typing import Optional
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    size = len(nums)
    res = [0] * size

    prefix = 1 # prefix of element 0 is 1
    # from 0 to size - 1
    # save in res all prefix results
    for i in range(size):
        res[i] = prefix
        prefix *= nums[i]
    print(res)

    postfix = 1 # postfix of last element is also 1
    # from size - 1 to 0
    # calculate all postfix multipling them for the correspondant prefixes
    # calculated before
    for i in range(size - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    print(res)


print(productExceptSelf([1, 2, 3, 4]))
