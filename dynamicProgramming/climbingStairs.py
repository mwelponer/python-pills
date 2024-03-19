from typing import Optional

#  0  1  2  3  4  5
#                __
#             __|
#          __|
#       __|
#    __|
# __|
#
#  8  5  3  2  1  1
#             one two
# ways of reaching step 5 from the current step is the sum of two previous ways
# (e.g. 8 = 5+3)
# NB: if I am on step 5 there is 1 way of reaching 5, that is doing no step

# bottom-up dynamic programming solution, using memoaization
def climbStairs(n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


print(climbStairs(3))
