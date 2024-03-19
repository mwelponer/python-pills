from typing import Optional
from typing import List
import sys

# setting path
sys.path.append('../neetcode')
from utils import ListNode


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:

    dummy = ListNode(0, head)
    ptr = dummy
    fast = head

    while fast and n > 0:
        fast = fast.next
        n -= 1

    while fast:
        fast = fast.next
        ptr = ptr.next

    ptr.next = ptr.next.next

    return dummy.next


lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(lst)

print(removeNthFromEnd(lst, 2))
