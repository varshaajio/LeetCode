class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total_sum = sum(nums)
        target = total_sum % p
        
        
        if target == 0:
            return 0
        
        mod_map = {0: -1}
        
        current_sum = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            current_sum += num
            current_mod = current_sum % p
            needed_mod = (current_mod - target) % p
            
            if needed_mod in mod_map:
                subarray_len = i - mod_map[needed_mod]
                min_len = min(min_len, subarray_len)
            
            
            mod_map[current_mod] = i
         
        return min_len if min_len < len(nums) else -1    
