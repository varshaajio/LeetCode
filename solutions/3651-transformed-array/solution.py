class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            if nums[i] == 0:
                result[i] = 0
            else:
                # (current index + jump) modulo array length
                # Handles both positive (right) and negative (left) jumps
                landing_index = (i + nums[i]) % n
                result[i] = nums[landing_index]
                
        return result
