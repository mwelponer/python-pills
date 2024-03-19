from typing import Optional
import sys

# setting path
sys.path.append('../neetcode')
from utils import ListNode


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    # 1. divide the list in two parts
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow.next now is the pointer to the second part


    # 2. reverse second half
    two = slow.next
    slow.next = None
    prev = None
    while two:
        tmp = two.next
        two.next = prev

        prev = two
        two = tmp
    # prev now points to the inverted second half


    # 3. merge two parts
    one, two = head, prev

    while two:
        oneNxt, twoNxt = one.next, two.next
        one.next = two
        two.next = oneNxt
        one, two = oneNxt, twoNxt
    # head still points to the rearranged linked list


list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(list1)
reorderList(list1)
print(list1)

# list2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# print(list2)
# reorderList(list2)
