from collections import Counter
import bisect

class Solution(object):
    def maximumTotalDamage(self, power):
        freq = Counter(power)
        unique = sorted(freq)
        n = len(unique)
        
        damage = [x * freq[x] for x in unique]
        dp = [0] * n
        
        for i in range(n):
            # Option 1: take current power
            take = damage[i]
            # find last index j with unique[j] <= unique[i] - 3
            j = bisect.bisect_right(unique, unique[i] - 3) - 1
            if j >= 0:
                take += dp[j]
            # Option 2: skip current power
            skip = dp[i-1] if i > 0 else 0
            dp[i] = max(take, skip)
        
        return dp[-1]

