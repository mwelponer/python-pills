from typing import Optional
from typing import List

def maxSubArray(nums: List[int]) -> int:
    maxSub = nums[0]

    sum = nums[0]
    for i in range(1, len(nums)):
        sum = sum + nums[i] if sum + nums[i] > nums[i] else nums[i]
        #sum = max(sum + nums[i], nums[i])
        maxSub = maxSub if maxSub > sum else sum
        #maxSub = max(maxSub, sum)

    return maxSub


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
