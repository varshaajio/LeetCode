class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0
        
        for i in range(1, n + 1):
            # i.bit_length() tells us how many positions to shift res
            # Example: if i=2 ("10"), bit_length is 2. 
            # We shift res by 2 and add 2.
            res = ((res << i.bit_length()) + i) % MOD
            
        return res
