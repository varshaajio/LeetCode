class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True
        
        ops = 0
        
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0
            
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            
            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            ops += 1
        
        return ops

