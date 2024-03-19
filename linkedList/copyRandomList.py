from typing import Optional
from typing import List

# import sys

# # setting path
# sys.path.append('../neetcode')
# from utils import ListNode


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        s = "["
        while self:
            if self.random:
                s += f"[{self.val}, {self.random.val}], "
            else:
                s += f"[{self.val}, null], "
            self = self.next
        return s[:-2] + "]"


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':

    # map old nodes with cloned ones
    hm = {None : None}

    # first pass to create cloned nodes
    ptr = head
    while ptr:
        hm[ptr] = Node(ptr.val)
        ptr = ptr.next

    # second pass to copy the next and random links
    ptr = head
    while ptr:
        copy = hm[ptr]
        copy.next = hm[ptr.next]
        copy.random = hm[ptr.random]
        ptr = ptr.next

    return hm[head]


n0 = Node(7)
n1 = Node(13)
n2 = Node(11)
n3 = Node(10)
n4 = Node(1)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None
n0.random = None
n1.random = n0
n2.random = n4
n3.random = n2
n4.random = n0

print(n0)
print(copyRandomList(n0))
