from typing import Optional

# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#
#     map = {}
#
#     # fill the hashmap with s chars
#     for c in s:
#         # increment or put 0 if not present
#         map[c] = 1 + map.get(c, 0)
#     # remove occurrences of chars from the hashmap
#     for c in t:
#         if c not in map:
#             return False
#         if map[c] == 1:
#             map.pop(c)
#         else:
#             map[c] = map[c] - 1
#
#     # if map is empty then return True
#     return not len(map)

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
