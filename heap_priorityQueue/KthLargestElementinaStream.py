from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # private member variables inside __init__
        self.minHeap, self.k = nums, k

        heapq.heapify(self.minHeap) # order pqueue in lg(n)
        for i in range(len(self.minHeap) - k): # we just need to remember k elements
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # add the new element

        if len(self.minHeap) > self.k: # if we have k+1 elements remove smallest
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


kl = KthLargest(3, [4, 5, 8, 2])
print(kl.add(3))
print(kl.add(5))
print(kl.add(10))
print(kl.add(9))
print(kl.add(4))
