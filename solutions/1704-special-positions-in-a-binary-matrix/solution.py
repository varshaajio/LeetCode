from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Step 1: Compute row sums and column sums
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        # Step 2: Count special positions
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1
        return count

