from collections import Counter

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        n = len(nums)
        if n == 0:
            return 0

        freq = Counter(nums)
        
        events = []
        for x in nums:
            L = x - k
            R = x + k + 1  
            events.append((L, 1))
            events.append((R, -1))

        events.sort()
        
        cover_at_value = {}
        cover = 0
        idx = 0
        m = len(events)
        
        unique_vals = sorted(freq.keys())
        ptr_vals = 0
        
        while idx < m or ptr_vals < len(unique_vals):
            next_event_pos = events[idx][0] if idx < m else None
            next_val_pos = unique_vals[ptr_vals] if ptr_vals < len(unique_vals) else None

            if next_event_pos is not None and (next_val_pos is None or next_event_pos <= next_val_pos):
                
                pos = next_event_pos
                while idx < m and events[idx][0] == pos:
                    cover += events[idx][1]
                    idx += 1
                
            else:
                
                vpos = next_val_pos
                
                
                cover_at_value[vpos] = cover
                ptr_vals += 1

        
        
        if len(cover_at_value) != len(unique_vals):
            cover_at_value = {}
            cover = 0
            idx = 0
            ev_pos_list = events
            vals = unique_vals
            vi = 0
            while vi < len(vals):
                v = vals[vi]
                while idx < m and ev_pos_list[idx][0] <= v:
                    cover += ev_pos_list[idx][1]
                    idx += 1
                cover_at_value[v] = cover
                vi += 1

        
        cover = 0
        max_cover = 0
        for pos, delta in events:
            cover += delta
            if cover > max_cover:
                max_cover = cover

        best = 0
        
        best = max(best, min(max_cover, numOperations))

        
        for v, f in freq.items():
            cov = cover_at_value.get(v, 0)
            candidate = min(cov, f + numOperations)
            if candidate > best:
                best = candidate

        return best

