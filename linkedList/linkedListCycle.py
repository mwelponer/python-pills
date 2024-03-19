from typing import Optional
from typing import List
import sys

# setting path
sys.path.append('../neetcode')
from utils import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

list = ListNode(3)
l2 = ListNode(2)
l0 = ListNode(0, ListNode(-4, l2))
l2.next = l0
list.next = l2

print(hasCycle(list))
