from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        n = len(nums)
        # We need to pick k-1 elements from a window of size dist + 1
        m = k - 1 
        window_size = dist + 1
        
        # Left set (S) will keep the m smallest, Right set (L) the rest
        S = SortedList()
        L = SortedList()
        current_sum = 0
        
        def add(val):
            nonlocal current_sum
            S.add(val)
            current_sum += val
            if len(S) > m:
                removed = S.pop() # Remove the largest from the "small" set
                current_sum -= removed
                L.add(removed)

        def remove(val):
            nonlocal current_sum
            if val in S:
                S.remove(val)
                current_sum -= val
                if L:
                    moved = L.pop(0) # Pull the smallest from the "large" set
                    current_sum += moved
                    S.add(moved)
            else:
                L.remove(val)

        # Initialize the first window: nums[1] to nums[dist + 1]
        for i in range(1, window_size + 1):
            add(nums[i])
            
        ans = current_sum
        
        # Slide the window across the rest of the array
        for i in range(window_size + 1, n):
            remove(nums[i - window_size])
            add(nums[i])
            ans = min(ans, current_sum)
            
        return ans + nums[0]
