from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # row_sum[i][j] stores sum of grid[i][0...j-1]
        row_sum = [[0] * (n + 1) for _ in range(m)]
        # col_sum[i][j] stores sum of grid[0...i-1][j]
        col_sum = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]
        
        def is_magic(r, c, k):
            # Use the first row sum as the reference target
            target = row_sum[r][c + k] - row_sum[r][c]
            
            # Check all row sums (starting from second row)
            for i in range(r + 1, r + k):
                if row_sum[i][c + k] - row_sum[i][c] != target:
                    return False
            
            # Check all column sums
            for j in range(c, c + k):
                if col_sum[r + k][j] - col_sum[r][j] != target:
                    return False
            
            # Check main diagonal
            d1 = 0
            for i in range(k):
                d1 += grid[r + i][c + i]
            if d1 != target:
                return False
            
            # Check anti-diagonal
            d2 = 0
            for i in range(k):
                d2 += grid[r + i][c + k - 1 - i]
            if d2 != target:
                return False
            
            return True

        # Check from largest possible side length k down to 2
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        
        return 1
