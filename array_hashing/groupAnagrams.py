from typing import List
from typing import Optional
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list) # key = [0] * 26, value = list of anagrams

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        # count being itself a list needs to be converted to a tuple
        # to be used as key of the defaultdict
        res[tuple(count)].append(s) # append string s to the list of anagrams

    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
