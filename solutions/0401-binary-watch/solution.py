class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        # Iterate through all possible hours (0-11)
        for h in range(12):
            # Iterate through all possible minutes (0-59)
            for m in range(60):
                # bin(n).count('1') counts the number of set bits in the integer
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    # Format: h as is, m with a leading zero if it's less than 10
                    result.append(f"{h}:{m:02d}")
                    
        return result
