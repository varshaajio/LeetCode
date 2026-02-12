class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            # Frequency map for the current window starting at i
            counts = {}
            for j in range(i, n):
                char = s[j]
                counts[char] = counts.get(char, 0) + 1
                
                # Get all frequencies currently in the map
                freq_values = counts.values()
                
                # Check if all frequencies are the same
                # Using a set is a quick way to see if all values are identical
                if len(set(freq_values)) == 1:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
