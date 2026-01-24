class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Step 1: Sort the numbers
        nums.sort()
        
        max_sum = 0
        n = len(nums)
        
        # Step 2: Pair the smallest with the largest
        for i in range(n // 2):
            current_pair_sum = nums[i] + nums[n - 1 - i]
            # Step 3: Update the minimized maximum
            max_sum = max(max_sum, current_pair_sum)
            
        return max_sum
