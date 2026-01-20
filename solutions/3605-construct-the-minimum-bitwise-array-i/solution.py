class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            # If n is 2, no ans[i] OR (ans[i] + 1) can equal 2.
            # (Because x OR (x+1) is almost always odd, and for x=0 it is 1)
            if n == 2:
                ans.append(-1)
                continue
            
            # We look for the first 0 from the right in the binary of n.
            # The bit to flip is the one just before the end of the 
            # trailing sequence of 1s.
            # Example: 11 is 1011. Trailing 1s are at index 0 and 1.
            # We flip the bit at index 1 to 0 -> 1001 (9).
            
            # Find the first 0 bit from the right
            # We can do this by checking bits one by one
            for i in range(31):
                # Check if the i-th bit is 0
                if not (n & (1 << i)):
                    # The bit we need to flip to 0 is the (i-1)-th bit
                    # This bit must be a 1 for the condition to work
                    res = n ^ (1 << (i - 1))
                    ans.append(res)
                    break
        return ans
