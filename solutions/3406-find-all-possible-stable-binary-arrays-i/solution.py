class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][0] = ways to use i zeros and j ones, ending in 0
        # dp[i][j][1] = ways to use i zeros and j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: filling only zeros or only ones within the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Transition for ending in 0
                # We can add a 0 to any valid sequence ending in 0 or 1
                val0 = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    # Subtract sequences that would result in limit + 1 zeros
                    val0 = (val0 - dp[i-limit-1][j][1] + MOD) % MOD
                dp[i][j][0] = val0
                
                # Transition for ending in 1
                val1 = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    # Subtract sequences that would result in limit + 1 ones
                    val1 = (val1 - dp[i][j-limit-1][0] + MOD) % MOD
                dp[i][j][1] = val1
                
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
