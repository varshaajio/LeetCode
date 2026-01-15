class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # Helper function to find the maximum gap size from a list of bars
        def get_max_gap(bars):
            # Sort the bars to easily find consecutive sequences
            bars.sort()
            
            max_consecutive = 1
            current_consecutive = 1
            
            # Iterate through the bars to find the longest consecutive sequence
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_consecutive += 1
                else:
                    current_consecutive = 1
                max_consecutive = max(max_consecutive, current_consecutive)
            
            # The gap size is always the number of removed bars + 1
            return max_consecutive + 1

        # Calculate max height and max width
        max_height = get_max_gap(hBars)
        max_width = get_max_gap(vBars)
        
        # The largest square side is determined by the smaller dimension
        side = min(max_height, max_width)
        
        return side * side
