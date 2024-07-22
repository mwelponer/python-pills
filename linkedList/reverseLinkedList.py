from typing import Optional
import sys, os

# setting path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_dir)
from utils import ListNode


# def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
#     res = None
#     while head:
#         #print(head.val)
#         n = ListNode(head.val)
#         n.next = res
#         res = n
#         head = head.next
#
#     return res

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prv = None

    while head:
        nxt = head.next # save next for later

        head.next = prv # invert the link

        # prepare variables for the next iteration
        prv = head
        head = nxt

    return prv # return prv because in the last iteration head is
    # set to nxt, head is 5 and next of 5 is Null



head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(head)

print(reverseList(head))
