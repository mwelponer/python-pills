"""
Encode and Decode Strings
=========================
Description
Design an algorithm to encode a list of strings to a string. The encoded string
is then sent over the network and is decoded back to the original list of
strings.

Please implement encode and decode

Example 1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""
from typing import Optional
from typing import List

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs: List[str]) -> str:
        # write your code here
        out = ""
        for word in strs:
            out = out + str(len(word)) + '%' + word

        print(out)
        return out


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str: str) -> List[str]:
        # write your code here
        i, res = 0, []

        while i < len(str):
            j = i
            while str[j] != '%':
                j += 1
            wLength = int(str[i:j])
            res.append(str[j + 1:j + 1 + wLength])
            i = j + 1 + wLength

        print(res)
        return res


s = Solution()
encoded = s.encode(["lint","code","love","you"])
s.decode(encoded)
