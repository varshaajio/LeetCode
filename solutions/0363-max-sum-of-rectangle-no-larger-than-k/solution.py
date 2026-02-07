from typing import List
import bisect
import math

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = -float('inf')
        
        # Follow-up optimization: 
        # If rows are much larger than cols, iterate over columns (O(n^2 * m log m)).
        # If cols are much larger, iterating over rows is better.
        # We ensure the outer loop iterates over the smaller dimension.
        if m > n:
            # Iterate over column pairs
            for left in range(n):
                # row_sums stores the sum of each row between col 'left' and 'right'
                row_sums = [0] * m
                for right in range(left, n):
                    # Update row_sums with the new column
                    for i in range(m):
                        row_sums[i] += matrix[i][right]
                    
                    # Now find the max subarray sum <= k in this 1D array (row_sums)
                    res = max(res, self.maxSumSubarrayNoLargerThanK(row_sums, k))
                    if res == k: return k # Early exit optimization
        else:
            # Iterate over row pairs (transpose logic effectively)
            for top in range(m):
                col_sums = [0] * n
                for bottom in range(top, m):
                    for i in range(n):
                        col_sums[i] += matrix[bottom][i]
                    
                    res = max(res, self.maxSumSubarrayNoLargerThanK(col_sums, k))
                    if res == k: return k
                    
        return res

    def maxSumSubarrayNoLargerThanK(self, nums: List[int], k: int) -> int:
        # Optimization: First try Kadane's algorithm (O(N)).
        # If the max subarray sum (without constraints) is <= k, 
        # then that is effectively the answer for this strip.
        current_sum = 0
        max_kadane = -float('inf')
        for x in nums:
            current_sum = max(x, current_sum + x)
            max_kadane = max(max_kadane, current_sum)
        
        if max_kadane <= k:
            return max_kadane

        # Fallback: Standard O(N log N) approach using bisect
        # We need curr_sum - prev_sum <= k  =>  prev_sum >= curr_sum - k
        res = -float('inf')
        prefix_sum = 0
        # Sorted list of prefix sums seen so far. Start with 0 (empty prefix).
        sorted_prefixes = [0]
        
        for x in nums:
            prefix_sum += x
            
            # We want the smallest prefix >= prefix_sum - k
            target = prefix_sum - k
            idx = bisect.bisect_left(sorted_prefixes, target)
            
            # If such a prefix exists, it's a valid candidate
            if idx < len(sorted_prefixes):
                res = max(res, prefix_sum - sorted_prefixes[idx])
            
            # Insert current prefix into sorted list to maintain order
            bisect.insort(sorted_prefixes, prefix_sum)
            
        return res
