class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        max_val = 0
        for row in grid:
            max_val = max(max_val, max(row))
        
        # dp[t][i][j] initialized to infinity
        # We use a 3D array or toggle between two 2D arrays to save space
        dp = [[[float('inf')] * n for _ in range(m)] for _ in range(k + 1)]
        
        # Starting point: cost is 0 as per example
        dp[0][0][0] = 0
        
        for t in range(k + 1):
            # 1. Handle Normal Moves for current level t
            # (Standard 2D DP for Right/Down movement)
            for r in range(m):
                for c in range(n):
                    if r > 0:
                        dp[t][r][c] = min(dp[t][r][c], dp[t][r-1][c] + grid[r][c])
                    if c > 0:
                        dp[t][r][c] = min(dp[t][r][c], dp[t][r][c-1] + grid[r][c])
            
            # 2. Prepare Teleportation for next level t+1
            if t < k:
                # Find min cost at level t for each grid value
                min_cost_at_val = [float('inf')] * (max_val + 1)
                for r in range(m):
                    for c in range(n):
                        if dp[t][r][c] != float('inf'):
                            v = grid[r][c]
                            min_cost_at_val[v] = min(min_cost_at_val[v], dp[t][r][c])
                
                # Compute suffix minimums
                # suffix_min[v] = min cost to reach a cell with value >= v
                suffix_min = [float('inf')] * (max_val + 2)
                for v in range(max_val, -1, -1):
                    suffix_min[v] = min(min_cost_at_val[v], suffix_min[v+1])
                
                # Teleport to every cell for the next level
                for r in range(m):
                    for c in range(n):
                        dp[t+1][r][c] = min(dp[t+1][r][c], suffix_min[grid[r][c]])

        # The answer is the minimum cost to reach (m-1, n-1) across all k levels
        ans = min(dp[t][m-1][n-1] for t in range(k + 1))
        return ans
