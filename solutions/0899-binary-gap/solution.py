class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_pos = -1
        current_pos = 0
        
        while n > 0:
            # Check if the current least significant bit is a 1
            if n & 1:
                if last_pos != -1:
                    # Update max_gap with the distance from the previous 1
                    max_gap = max(max_gap, current_pos - last_pos)
                # Update the position of the last seen 1
                last_pos = current_pos
            
            # Right shift n to check the next bit and increment position counter
            n >>= 1
            current_pos += 1
            
        return max_gap
