class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Calculate the total number of unique codes required
        required_count = 1 << k  # This is equivalent to 2^k
        
        # Use a set to store unique substrings of length k
        seen_codes = set()
        
        # Iterate through s with a sliding window of size k
        # We stop at len(s) - k + 1 to ensure the last window is valid
        for i in range(len(s) - k + 1):
            code = s[i : i + k]
            seen_codes.add(code)
            
            # Optimization: If we've already found all codes, return True early
            if len(seen_codes) == required_count:
                return True
                
        # If the loop finishes and we haven't reached the required count
        return len(seen_codes) == required_count
