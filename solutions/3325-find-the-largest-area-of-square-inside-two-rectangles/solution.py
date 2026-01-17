from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_side = 0
        n = len(bottomLeft)
        
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the boundaries of the intersection rectangle
                inter_x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                inter_y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                inter_x2 = min(topRight[i][0], topRight[j][0])
                inter_y2 = min(topRight[i][1], topRight[j][1])
                
                # Check if there is a valid intersection
                if inter_x2 > inter_x1 and inter_y2 > inter_y1:
                    width = inter_x2 - inter_x1
                    height = inter_y2 - inter_y1
                    
                    # The largest square side in this intersection is the smaller of width or height
                    current_side = min(width, height)
                    max_side = max(max_side, current_side)
                    
        return max_side * max_side
