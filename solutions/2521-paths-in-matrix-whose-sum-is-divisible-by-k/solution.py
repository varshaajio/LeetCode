class Solution(object):
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[j][r] = number of ways to reach cell in current processed row at column j with remainder r
        dp = [ [0] * k for _ in range(n) ]

        # initialize first cell
        dp[0][ grid[0][0] % k ] = 1

        # initialize first row (only from left)
        for j in range(1, n):
            val = grid[0][j]
            for r in range(k):
                if dp[j-1][r]:
                    newr = (r + val) % k
                    dp[j][newr] = (dp[j][newr] + dp[j-1][r]) % MOD

        # process remaining rows
        for i in range(1, m):
            new_dp = [ [0] * k for _ in range(n) ]

            # first column of this row: can only come from top (dp[0])
            val = grid[i][0]
            for r in range(k):
                if dp[0][r]:
                    newr = (r + val) % k
                    new_dp[0][newr] = (new_dp[0][newr] + dp[0][r]) % MOD

            # remaining columns: can come from top (dp[j]) or left (new_dp[j-1])
            for j in range(1, n):
                val = grid[i][j]
                # from top
                for r in range(k):
                    if dp[j][r]:
                        newr = (r + val) % k
                        new_dp[j][newr] = (new_dp[j][newr] + dp[j][r]) % MOD
                # from left
                for r in range(k):
                    if new_dp[j-1][r]:
                        newr = (r + val) % k
                        new_dp[j][newr] = (new_dp[j][newr] + new_dp[j-1][r]) % MOD

            dp = new_dp

        return dp[n-1][0] % MOD

