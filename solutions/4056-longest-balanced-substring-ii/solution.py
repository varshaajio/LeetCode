class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        # Case 1: Substrings with exactly 1 distinct character
        # (e.g., "aaaa")
        current_run = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                current_run += 1
            else:
                max_len = max(max_len, current_run)
                current_run = 1
        max_len = max(max_len, current_run)

        # Case 2: Substrings with exactly 2 distinct characters
        # We check pairs (a,b), (b,c), and (a,c).
        # Substrings must NOT contain the third character.
        for p1, p2, p3 in [('a', 'b', 'c'), ('b', 'c', 'a'), ('a', 'c', 'b')]:
            # Splitting by p3 ensures the resulting segments only contain p1 and p2
            for segment in s.split(p3):
                if not segment:
                    continue
                
                # Use a prefix difference map to find equal counts of p1 and p2
                diff_map = {0: -1}
                diff = 0
                for idx, char in enumerate(segment):
                    if char == p1:
                        diff += 1
                    else:
                        diff -= 1
                    
                    if diff in diff_map:
                        max_len = max(max_len, idx - diff_map[diff])
                    else:
                        diff_map[diff] = idx

        # Case 3: Substrings with exactly 3 distinct characters
        # Requirement: Count(a) == Count(b) == Count(c)
        # This is true if (Count(a) - Count(b) == 0) AND (Count(b) - Count(c) == 0)
        diff_map = {(0, 0): -1}
        ca, cb, cc = 0, 0, 0
        for i, char in enumerate(s):
            if char == 'a': ca += 1
            elif char == 'b': cb += 1
            else: cc += 1
            
            # The "state" is the relative difference between character counts
            state = (ca - cb, cb - cc)
            if state in diff_map:
                max_len = max(max_len, i - diff_map[state])
            else:
                diff_map[state] = i
                
        return max_len
