from typing import Optional
from collections import Counter


def characterReplacement(s: str, k: int) -> int:
    l, longest = 0, 0
    hmap = {}

    # l and r are initially set to 0,
    # expand the window
    for r in range(len(s)):
        # update the occurences
        hmap[s[r]] = hmap.get(s[r], 0) + 1

        # now len(window) - count of the most frequent char
        # gives us the count of changes we need to make
        # to have substring with all the same char

        # while k changes are not enough, left-shrink the window,
        # to make it valid i.e. decrement occurences
        # of l and move l right
        while r - l + 1 - max(hmap.values()) > k:
            hmap[s[l]] -= 1 # decrement s[l] in hmap
            l += 1

        # now window is valid so update longest
        longest = max(longest, r - l + 1)

    return longest


print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
print(characterReplacement("ABBB", 2))
