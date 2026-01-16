from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Add the implicit boundary fences
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        
        # Helper to get all possible differences (side lengths)
        def get_diffs(fences):
            fences.sort()
            diffs = set()
            for i in range(len(fences)):
                for j in range(i + 1, len(fences)):
                    diffs.add(fences[j] - fences[i])
            return diffs
        
        h_diffs = get_diffs(hFences)
        v_diffs = get_diffs(vFences)
        
        max_side = -1
        
        # Check for the largest common difference
        for side in v_diffs:
            if side in h_diffs:
                max_side = max(max_side, side)
        
        if max_side == -1:
            return -1
        
        # Return area modulo 10^9 + 7
        return (max_side * max_side) % (10**9 + 7)
