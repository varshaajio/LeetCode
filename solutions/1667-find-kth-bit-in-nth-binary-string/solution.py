class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: S1 is "0"
        if n == 1:
            return "0"
        
        # Calculate the total length of Sn: 2^n - 1
        length = (1 << n) - 1
        mid = (length // 2) + 1
        
        if k == mid:
            # The middle bit added in Si = Si-1 + "1" + reverse(invert(Si-1))
            return "1"
        elif k < mid:
            # k is in the first half, which is just Sn-1
            return self.findKthBit(n - 1, k)
        else:
            # k is in the second half. 
            # We find the mirrored position in the first half:
            # mirrored_k = total_length - k + 1
            mirrored_k = length - k + 1
            res = self.findKthBit(n - 1, mirrored_k)
            # The second half is the reverse(invert(Sn-1)), so we flip the bit
            return "1" if res == "0" else "0"
