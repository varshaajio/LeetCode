class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        left = 0
        max_kept = 0
        
        # Sliding window with two pointers
        for right in range(n):
            # While the window is not balanced, shrink from the left
            while nums[right] > nums[left] * k:
                left += 1
            
            # Calculate how many elements are currently in the balanced window
            current_window_size = right - left + 1
            max_kept = max(max_kept, current_window_size)
                
        return n - max_kept
