from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
            
        # --- 1. Calculate P (Valid Parallelograms) ---
        # Structure: map[midpoint][slope] = count
        midpoint_slope_map = defaultdict(lambda: defaultdict(int))
        
        # --- 2. Prepare for S (Slope Grouping) ---
        # Structure: map[slope] = list of (index_i, index_j, line_intercept)
        slope_map = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # --- Geometry Helpers ---
                # Midpoint (doubled to keep int): (x1+x2, y1+y2)
                mid_x, mid_y = x1 + x2, y1 + y2
                
                # Slope (dx, dy) normalized
                dx, dy = x1 - x2, y1 - y2
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0 and dy < 0:
                    dy = -dy
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Line Intercept (C in dx*Y - dy*X = C)
                # Used to identify if segments are on the exact same infinite line
                c_val = dx * y1 - dy * x1
                
                # Store data
                midpoint_slope_map[(mid_x, mid_y)][(dx, dy)] += 1
                slope_map[(dx, dy)].append((i, j, c_val))

        # --- Calculate Total Parallelograms (P) ---
        total_parallelograms = 0
        for slopes in midpoint_slope_map.values():
            # Total segments sharing this midpoint
            total_segments = sum(slopes.values())
            # All possible pairs sharing this midpoint
            total_pairs = total_segments * (total_segments - 1) // 2
            
            # Subtract pairs that share midpoint AND slope (Collinear)
            degenerate_pairs = 0
            for count in slopes.values():
                degenerate_pairs += count * (count - 1) // 2
            
            total_parallelograms += (total_pairs - degenerate_pairs)

        # --- Calculate Total Trapezoid Candidates (S) ---
        # S counts sets of 4 points with at least one parallel pair.
        # This includes Parallelograms twice (once for each parallel pair).
        total_trapezoid_counts = 0
        
        for segments in slope_map.values():
            k = len(segments)
            if k < 2:
                continue
            
            # Start with all pairs of segments having the same slope
            current_valid_pairs = k * (k - 1) // 2
            
            line_counts = defaultdict(int)
            point_counts = defaultdict(int)
            segments_by_line = defaultdict(list)
            
            for u, v, c_val in segments:
                line_counts[c_val] += 1
                point_counts[u] += 1
                point_counts[v] += 1
                segments_by_line[c_val].append((u, v))
            
            # Inclusion-Exclusion Principle:
            # Valid = Total - Collinear - SharedVertex + Intersection
            
            # 1. Subtract Collinear pairs (Same line C)
            for count in line_counts.values():
                current_valid_pairs -= count * (count - 1) // 2
            
            # 2. Subtract Shared Vertex pairs (Same endpoint)
            for count in point_counts.values():
                current_valid_pairs -= count * (count - 1) // 2
                
            # 3. Add Intersection (Pairs that are BOTH Collinear AND Shared Vertex)
            # These were subtracted twice, so add back once.
            for line_segs in segments_by_line.values():
                local_pt_counts = defaultdict(int)
                for u, v in line_segs:
                    local_pt_counts[u] += 1
                    local_pt_counts[v] += 1
                
                for count in local_pt_counts.values():
                    current_valid_pairs += count * (count - 1) // 2
            
            total_trapezoid_counts += current_valid_pairs
            
        # Final Formula: (Trapezoids + 2*Parallelograms) - Parallelograms
        return total_trapezoid_counts - total_parallelograms
