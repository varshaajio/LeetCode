from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0
        
        n = len(strs)
        m = len(strs[0])
        
        # dp[i] will store the length of the longest valid subsequence 
        # ending at column index i.
        dp = [1] * m
        
        for i in range(m):
            for j in range(i):
                # Check if column j can precede column i for ALL strings
                is_valid = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        is_valid = False
                        break
                
                if is_valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The maximum number of columns we can keep
        max_kept = max(dp) if dp else 0
        
        # Minimum deletions = Total columns - Max kept columns
        return m - max_kept
