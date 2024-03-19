from typing import Optional
from typing import List
import sys

# setting path
sys.path.append('../neetcode')
from utils import ListNode


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if not list1: current.next = list2
    if not list2: current.next = list1

    return dummy.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
print(list1)
list2 = ListNode(1, ListNode(3, ListNode(4)))
print(list2)

print(mergeTwoLists(list1, list2))
