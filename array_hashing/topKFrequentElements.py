from typing import Optional
from typing import List
from collections import Counter
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums) # use Counter to get a map of nums frequencies in O(n)

    maxHeap = [] # put entries in a maxheap ordered according to frequencies O(nLogN)
    for key, value in count.items():
        heapq.heappush(maxHeap, (-value, key))

    res = []
    # pop k elements key-s
    for i in range(k):
        res.append(heapq.heappop(maxHeap)[1])

    return res

def topKFrequentOptimized(nums: List[int], k: int) -> List[int]:
    count = Counter(nums) # key:value is num:frequency

    # array where at i pos I save the list of elements
    # appearing i times
    bucket = [[] for i in range(len(nums) + 1)]
    for num, freq in count.items():
        bucket[freq].append(num)

    res = []
    # from last element in bucket (higher index) remove elements
    # from non empty lists till we collect k elements 
    for i in range(len(bucket)-1, -1, -1):
        while bucket[i]:
            res.append(bucket[i].pop())
        if len(res) == k:
            return res



# print(topKFrequent([1,1,1,2,2,3], 2))
# print(topKFrequent([3,0,1,0], 1))

print(topKFrequentOptimized([1,1,1,2,2,3], 2))
print(topKFrequentOptimized([3,0,1,0], 1))
