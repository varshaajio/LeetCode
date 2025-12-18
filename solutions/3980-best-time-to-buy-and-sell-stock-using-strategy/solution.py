from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        base_profit = 0
        for p, s in zip(prices, strategy):
            base_profit += p * s
            
        # We want to find the window [i, i + k - 1] that maximizes the gain.
        # Gain = Sum_{j=i}^{i+k/2-1} (0 - strategy[j])*prices[j] 
        #        + Sum_{j=i+k/2}^{i+k-1} (1 - strategy[j])*prices[j]
        
        current_delta = 0
        half_k = k // 2
        
        # Initialize the delta for the first window starting at index 0
        for i in range(k):
            if i < half_k:
                # First k/2 elements become 0
                current_delta += (0 - strategy[i]) * prices[i]
            else:
                # Last k/2 elements become 1
                current_delta += (1 - strategy[i]) * prices[i]
        
        max_delta = current_delta
        
        # Slide the window across the arrays
        # The window is [i, i + k - 1]
        for i in range(1, n - k + 1):
            # Remove the effect of the element that is sliding out (at i-1)
            # That element was in the "first half" of the previous window
            current_delta -= (0 - strategy[i - 1]) * prices[i - 1]
            
            # The element that was at the start of the "second half" (i + half_k - 1)
            # now moves into the "first half". 
            mid_idx = i + half_k - 1
            # Subtract its old 'second half' contribution and add its 'first half' contribution
            current_delta -= (1 - strategy[mid_idx]) * prices[mid_idx]
            current_delta += (0 - strategy[mid_idx]) * prices[mid_idx]
            
            # Add the effect of the new element sliding in (at i + k - 1)
            # This element enters the "second half"
            new_idx = i + k - 1
            current_delta += (1 - strategy[new_idx]) * prices[new_idx]
            
            max_delta = max(max_delta, current_delta)
            
        # We can either take the best modification or do nothing (delta = 0)
        return base_profit + max(0, max_delta)
