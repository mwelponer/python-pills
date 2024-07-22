from typing import Optional
from typing import List
import sys, os

# setting path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_dir)
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
