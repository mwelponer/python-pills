from typing import Optional


class MinStack:

    def __init__(self):
        self.stack = []
        self.minsStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minsStack:
            self.minsStack.append(min(val, self.minsStack[-1]))
        else:
            self.minsStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minsStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.minsStack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2
