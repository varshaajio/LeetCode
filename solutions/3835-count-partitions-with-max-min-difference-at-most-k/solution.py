from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # dp[i] represents the number of ways to partition the prefix nums[:i]
        # Size is n + 1 because dp[0] is the base case (empty prefix)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # dp_prefix[i] stores the sum of dp[0]...dp[i-1]
        # This allows us to calculate the sum of a range in O(1)
        dp_prefix = [0] * (n + 2)
        dp_prefix[1] = 1  # prefix sum up to dp[0]
        
        # Monotonic deques to store indices of potential max and min values
        min_deque = deque()
        max_deque = deque()
        
        left = 0
        
        for i in range(n):
            # 1. Update Max Deque: Remove indices with values <= current
            while max_deque and nums[max_deque[-1]] <= nums[i]:
                max_deque.pop()
            max_deque.append(i)
            
            # 2. Update Min Deque: Remove indices with values >= current
            while min_deque and nums[min_deque[-1]] >= nums[i]:
                min_deque.pop()
            min_deque.append(i)
            
            # 3. Shrink window from the left if validity condition is broken
            # condition: max - min > k
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                left += 1
                # Remove indices from deques if they fall out of the new window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # 4. Calculate DP[i+1]
            # The valid last segments end at 'i' and can start anywhere from 'left' to 'i'.
            # If the last segment is nums[j...i], we must have partitioned nums[:j] previously.
            # So we sum dp[j] for all j in range [left, i].
            
            # Using prefix sums: sum(dp[left]...dp[i]) 
            # = dp_prefix[i+1] - dp_prefix[left]
            
            current_ways = (dp_prefix[i+1] - dp_prefix[left]) % MOD
            
            dp[i+1] = current_ways
            
            # Update prefix sum for the next iteration
            dp_prefix[i+2] = (dp_prefix[i+1] + current_ways) % MOD
            
        return dp[n]
