from typing import Optional


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    count1, count2 = [0] * 26, [0] * 26

    for i in range(len(s1)):
        count1[ord(s1[i]) - ord("a")] += 1
        count2[ord(s2[i]) - ord("a")] += 1
    # print(count1)
    # print(count2)

    # matches with first window
    matches = 0
    for i in range(26):
        matches += 1 if count1[i] == count2[i] else 0
    # print("matches", matches)
    # check if we have already won
    if matches == 26:
        return True

    # otherwise move window and update matches
    l, r = 1, len(s1) # move window
    while r < len(s2):
        # remove l - 1
        rem = ord(s2[l - 1]) - ord("a")
        if count1[rem] == count2[rem]: # if there was a match
            matches -= 1 # decrement matches
        count2[rem] -= 1 # remove left
        if count1[rem] == count2[rem]: # if we have a match
            matches += 1 # increment matches
        # add r
        add = ord(s2[r]) - ord("a")
        if count1[add] == count2[add]: # if there was a match
            matches -= 1 # decrement matches
        count2[add] += 1 # add right
        if count1[add] == count2[add]: # if we have a match
            matches += 1 # increment matches
        # print(count2)
        # print("matches", matches)

        if matches == 26:
            return True
        # move window
        l += 1
        r += 1

    return False


print(checkInclusion("a", "ab"))
# print(checkInclusion("ab", "eidbaooo"))
# print(checkInclusion("ab", "eidboaoo"))
# print(checkInclusion("adc", "dcda"))
