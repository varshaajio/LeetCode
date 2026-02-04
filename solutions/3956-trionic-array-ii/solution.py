class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0 
        
        # 1. Build L[i]: Max sum of strictly increasing subarray ending at i (len >= 2)
        # Initialize with -inf because strictly increasing subarray of len >= 2 might not exist ending at i
        L = [float('-inf')] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # We can either extend the previous best sequence (L[i-1])
                # OR start a fresh sequence of length 2 (nums[i-1] + nums[i])
                L[i] = nums[i] + max(nums[i-1], L[i-1])
        
        # 2. Build R[i]: Max sum of strictly increasing subarray starting at i (len >= 2)
        R = [float('-inf')] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                # We can either extend the next best sequence (R[i+1])
                # OR start a fresh sequence of length 2 (nums[i] + nums[i+1])
                R[i] = nums[i] + max(nums[i+1], R[i+1])
                
        # 3. Find Max Trionic Sum
        max_total = float('-inf')
        
        # We track the current strictly decreasing segment sum
        curr_dec_sum = nums[0]
        p = 0
        
        for q in range(1, n):
            if nums[q] < nums[q-1]:
                # Continue decreasing sequence
                curr_dec_sum += nums[q]
                
                # Check if this q can be a valid end of a trionic middle section
                # We need:
                # 1. A valid increasing sequence ending at p (L[p] > -inf)
                # 2. A valid increasing sequence starting at q (R[q] > -inf)
                if L[p] > float('-inf') and R[q] > float('-inf'):
                    # The sum is L[p] + (decreasing middle) + R[q]
                    # Note: L[p] includes nums[p], R[q] includes nums[q], curr_dec_sum includes both.
                    # We subtract them to avoid double counting.
                    total = L[p] + curr_dec_sum + R[q] - nums[p] - nums[q]
                    if total > max_total:
                        max_total = total
            else:
                # Decreasing sequence broken, reset p to current index (potential new peak)
                p = q
                curr_dec_sum = nums[q]
                
        return max_total
