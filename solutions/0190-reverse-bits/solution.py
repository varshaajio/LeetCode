class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # Iterate through all 32 bits
        for _ in range(32):
            # Shift result to the left to make room for the next bit
            res = (res << 1) | (n & 1)
            # Shift the input n to the right to process the next bit
            n >>= 1
        return res
