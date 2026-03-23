class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[-1, 1] for _ in range(n)] for _ in range(m)]
        print(dp)
        
        dp[0][0][0 if grid[0][0]>=0 else 1] = grid[0][0]

        for i in range(m):
            for j in range(n):
                v =  grid[i][j]
                if v > 0:
                    if i > 0:
                        nv = dp[i-1][j][0] * v
                        if nv >= 0:
                            dp[i][j][0] = nv
                        nv = dp[i-1][j][1] * v
                        if nv <= 0:
                            dp[i][j][1] = nv
                    if j > 0:
                        nv = dp[i][j-1][0] * v
                        if nv >= 0:
                            dp[i][j][0] = max(dp[i][j][0],nv)
                        nv = dp[i][j-1][1] * v
                        if nv <= 0:
                            dp[i][j][1] = min(dp[i][j][1], nv)
                elif v < 0:
                    if i > 0:
                        nv = dp[i-1][j][1] * v
                        if nv >= 0:
                            dp[i][j][0] = max(dp[i][j][0], nv)
                        nv = dp[i-1][j][0] * v
                        if nv <= 0:
                            dp[i][j][1] = min(dp[i][j][1], nv)
                    if j > 0:
                        nv = dp[i][j-1][1] * v
                        if nv >= 0:
                            dp[i][j][0] = max(dp[i][j][0], nv)
                        nv = dp[i][j-1][0] * v
                        if nv <= 0:
                            dp[i][j][1] = min(dp[i][j][1], nv)
                else:
                    dp[i][j] = [0, 0]
        return (dp[-1][-1][0] % (10**9+7)) if dp[-1][-1][0]>=0 else -1
