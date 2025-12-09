from typing import List
from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # 1. Initialize right_count with all frequencies
        #    These are the potential nums[k] elements (k > j)
        right_count = Counter(nums)
        
        # 2. Initialize left_count (initially empty)
        #    These are the potential nums[i] elements (i < j)
        left_count = Counter()
        
        total_triplets = 0
        
        # Iterate through the array, treating 'x' as nums[j]
        for x in nums:
            # Step 1: Remove x from the right side count 
            # (It is now the middle element 'j', so it can't be 'k')
            right_count[x] -= 1
            
            # Step 2: Calculate the required target value
            target = x * 2
            
            # Step 3: Count and multiply the combinations in O(1) time
            # We look up how many 'target's are on the left (i < j)
            # and how many 'target's are on the right (k > j)
            
            count_left = left_count.get(target, 0) # Use .get for safe lookup
            count_right = right_count.get(target, 0)
            
            # Only add if both counts are greater than zero
            if count_left > 0 and count_right > 0:
                total_triplets += count_left * count_right
                total_triplets %= MOD
            
            # Step 4: Add x to the left side count 
            # (For the next iteration, 'x' will be an element before j+1)
            left_count[x] += 1
            
        return total_triplets
