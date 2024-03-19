#from typing import Optional

def hammingWeight(n: int) -> int:
    count = 0

    while n: # while n is not 0
        n = n & (n - 1) # removes the less significant 1
        count += 1 # increment a counter

        # count += n & 1 # increment counter by less significant bit
        # n = n >> 1 # remove less significant bit

    return count


n = 0B00000000000000000000000000001011
print(hammingWeight(n))
