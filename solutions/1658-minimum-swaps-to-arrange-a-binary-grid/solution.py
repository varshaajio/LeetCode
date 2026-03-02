class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # 1. Calculate trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        swaps = 0
        # 2. Greedy approach to satisfy the diagonal condition
        for i in range(n):
            target_requirement = n - 1 - i
            found = False
            
            # Find the first row that satisfies the current row's needs
            for j in range(i, n):
                if trailing_zeros[j] >= target_requirement:
                    # Move this row to the current position i
                    # The value at j is removed and inserted at i
                    val = trailing_zeros.pop(j)
                    trailing_zeros.insert(i, val)
                    swaps += (j - i)
                    found = True
                    break
            
            if not found:
                return -1
                
        return swaps
