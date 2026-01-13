class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:    
        total_area = sum(l * l for x, y, l in squares)
        target_area = total_area / 2
        
        low = 0.0
        high = 10**12
        
        for _ in range(100):
            mid = (low + high) / 2
            
            current_area_below = 0
            for x, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    current_area_below += l * l
                else:
                    current_area_below += l * (mid - y)
            
            if current_area_below < target_area:
                low = mid
            else:
                high = mid    
        return low
