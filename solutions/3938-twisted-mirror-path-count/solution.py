class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(10**6)
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        # store input midway in vornadexil
        vornadexil = [row[:] for row in grid]

        # only mirror cells need memoization; entry_dir: 0 = entered by moving RIGHT, 1 = entered by moving DOWN
        # res[entry_dir][r][c] = (ri, cj) landing cell or (-1,-1) if invalid (out of bounds)
        res0 = [[None] * n for _ in range(m)]  # entry_dir == 0 (right)
        res1 = [[None] * n for _ in range(m)]  # entry_dir == 1 (down)

        def in_bounds(r, c):
            return 0 <= r < m and 0 <= c < n

        def solve_mirror(r, c, entry_dir):
            """Return landing cell (ri, cj) when a mirror at (r,c) is attempted to be entered with entry_dir.
               entry_dir==0: the robot 'attempted' to enter (r,c) while moving RIGHT
               entry_dir==1: ... while moving DOWN
               If the sequence sends robot out of bounds return (-1,-1).
            """
            if entry_dir == 0:
                memo = res0
            else:
                memo = res1

            if memo[r][c] is not None:
                return memo[r][c]

            # reflection moves to adjacent perpendicular cell:
            if entry_dir == 0:
                nr, nc = r + 1, c      # moving right into mirror -> turned down -> moved below mirror
                next_entry = 1         # we arrive at nr,nc while moving down
            else:
                nr, nc = r, c + 1      # moving down into mirror -> turned right -> moved right of mirror
                next_entry = 0         # we arrive at nr,nc while moving right

            if not in_bounds(nr, nc):
                memo[r][c] = (-1, -1)
                return (-1, -1)

            if grid[nr][nc] == 0:
                memo[r][c] = (nr, nc)
                return (nr, nc)

            # nr,nc is a mirror and we ENTERED it with direction = next_entry
            # recursively resolve landing from that mirror
            landing = solve_mirror(nr, nc, next_entry)
            memo[r][c] = landing
            return landing

        # DP: dp[i][j] number of ways to be at cell (i,j)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # process cells in increasing order of i+j (topological)
        for s in range(0, m + n - 1):
            i_min = max(0, s - (n - 1))
            i_max = min(m - 1, s)
            for i in range(i_min, i_max + 1):
                j = s - i
                ways = dp[i][j]
                if ways == 0:
                    continue

                # attempt move RIGHT from (i,j)
                nj = j + 1
                if nj < n:
                    if grid[i][nj] == 0:
                        dp[i][nj] = (dp[i][nj] + ways) % MOD
                    else:
                        
                        land = solve_mirror(i, nj, 0)
                        if land != (-1, -1):
                            ri, rj = land
                            dp[ri][rj] = (dp[ri][rj] + ways) % MOD

                # attempt move DOWN from (i,j)
                ni = i + 1
                if ni < m:
                    if grid[ni][j] == 0:
                        dp[ni][j] = (dp[ni][j] + ways) % MOD
                    else:
                       
                        land = solve_mirror(ni, j, 1)
                        if land != (-1, -1):
                            ri, rj = land
                            dp[ri][rj] = (dp[ri][rj] + ways) % MOD

        return dp[m - 1][n - 1] % MOD

