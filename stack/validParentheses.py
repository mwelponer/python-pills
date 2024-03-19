def isValid(s: str) -> bool:
    map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        # if it is an open parentesis
        if c in map.values():
            stack.append(c)
            continue
        else:
            # if stack is empty or c doesn't close last in stack
            if not stack or stack[-1] != map[c] :
                return False
            stack.pop()

    # return true if stack is empty
    return not stack


s = "()[]{}"
print(isValid(s))
s = "{()}"
print(isValid(s))
s = ""
print(isValid(s))
s = "("
print(isValid(s))
s = "]"
print(isValid(s))
s = "(]"
print(isValid(s))
