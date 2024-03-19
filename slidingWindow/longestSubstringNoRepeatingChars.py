from typing import Optional


def lengthOfLongestSubstring(s: str) -> int:
    l, longest = 0, 0
    hset = set()

    for r in range(len(s)):
        while s[r] in hset:
            print("  remove", s[l])
            hset.remove(s[l])
            l += 1

        print("add", s[r])
        hset.add(s[r])
        longest = max(longest, len(hset))
        print("longest:", longest)

    return longest


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("dvdf"))
