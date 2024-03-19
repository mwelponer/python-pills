from typing import List
from typing import Optional
from collections import Counter
import heapq
from collections import deque


def leastInterval(tasks: List[str], n: int) -> int:
    # create a list of occurrences using a Counter
    occ = Counter(tasks).values()
    print(occ)

    # negate each element and create a maxHeap
    occ = [-i for i in occ]
    heapq.heapify(occ)

    queue = deque()
    res = 0
    # starting from the most frequent
    # begin to process tasks
    while occ or queue:
        # if it is time to to process first in queue
        # remove it from queue and puh it into maxheap
        if queue and res == queue[0][1]:
            heapq.heappush(occ, queue.popleft()[0] * -1)

        # pop most frequent and increment res
        if occ:
            mostFr = heapq.heappop(occ) * -1
            if mostFr - 1 > 0:
                # add remaining occurrences of that process
                # to a queue, together with the time
                # in which we can process again that
                # type of task (res + n)
                queue.append((mostFr - 1, res + n + 1))
        res += 1

    return res


print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
