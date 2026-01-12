class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        # Iterate through the points starting from the second one
        for i in range(len(points) - 1):
            curr_p = points[i]
            next_p = points[i+1]
            
            # Calculate the distance for each dimension
            dx = abs(next_p[0] - curr_p[0])
            dy = abs(next_p[1] - curr_p[1])
            
            # The time taken is the maximum of the two distances
            total_time += max(dx, dy)
            
        return total_time
