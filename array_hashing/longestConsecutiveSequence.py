from typing import Optional
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    hset = set(nums) # create an hashset of all nums

    count = res = 0
    for n in nums:
        # if it is the beginning of a sequence
        if (n - 1) not in hset:
            count = 1 # starting from 1
            # increment each time we have a consecutive n
            while (n + count) in hset:
                count += 1
            # when the sequence is finished check if it is the longest
            res = max(res, count)

    return res


print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
