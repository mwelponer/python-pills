def alphanum(c: str):
    return  (   ord("a") <= ord(c) <= ord("z") or
                ord("A") <= ord(c) <= ord("Z") or
                ord("0") <= ord(c) <= ord("9")
            )


def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphanum(s[l]):
            l += 1
        while l < r and not alphanum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
