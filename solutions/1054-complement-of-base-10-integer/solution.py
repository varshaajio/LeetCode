class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # Determine the number of bits in n
        # bin(5) is '0b101', so len is 3
        bit_length = n.bit_length()
        
        # Create a mask of all 1s: (1 << 3) - 1 = 8 - 1 = 7 (111 in binary)
        mask = (1 << bit_length) - 1
        
        return n ^ mask
