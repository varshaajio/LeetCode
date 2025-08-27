class Solution:
    def lenOfVDiagonal(self, grid):
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        dp = [[[0] * m for _ in range(n)] for _ in range(4)]    
        turn = [[[0] * m for _ in range(n)] for _ in range(4)]  
        def expected_val(length):
            
            if length == 0:
                return 1
            return 2 if (length % 2 == 1) else 0

        ans = 0

        
        for d, (di, dj) in enumerate(dirs):
            rows = range(n) if di > 0 else range(n - 1, -1, -1)
            cols = range(m) if dj > 0 else range(m - 1, -1, -1)

            for i in rows:
                for j in cols:
                    prev_i, prev_j = i - di, j - dj
                    prev = dp[d][prev_i][prev_j] if (0 <= prev_i < n and 0 <= prev_j < m) else 0
                    cur = 1 if grid[i][j] == 1 else 0
                    if prev > 0:
                        need = expected_val(prev)
                        if grid[i][j] == need:
                            cur = max(cur, prev + 1)

                    dp[d][i][j] = cur
                    if cur > ans:
                        ans = cur

        
        for d, (di, dj) in enumerate(dirs):
            rows = range(n) if di > 0 else range(n - 1, -1, -1)
            cols = range(m) if dj > 0 else range(m - 1, -1, -1)
            pd = (d - 1) % 4  

            for i in rows:
                for j in cols:
                    prev_i, prev_j = i - di, j - dj

                    
                    prev_turn = turn[d][prev_i][prev_j] if (0 <= prev_i < n and 0 <= prev_j < m) else 0
                    if prev_turn > 0:
                        need = expected_val(prev_turn)
                        if grid[i][j] == need:
                            v = prev_turn + 1
                            if v > turn[d][i][j]:
                                turn[d][i][j] = v
                                if v > ans:
                                    ans = v

                    
                    pivot_i, pivot_j = prev_i, prev_j
                    if 0 <= pivot_i < n and 0 <= pivot_j < m:
                        prev_dp = dp[pd][pivot_i][pivot_j]
                        if prev_dp > 0:
                            need = expected_val(prev_dp)
                            if grid[i][j] == need:
                                v = prev_dp + 1
                                if v > turn[d][i][j]:
                                    turn[d][i][j] = v
                                    if v > ans:
                                        ans = v

        return ans

