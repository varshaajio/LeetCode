class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # --- Step 1: Coordinate Compression for X-axis ---
        # We need to map the large X coordinates to indices for the Segment Tree
        x_coords = set()
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
        
        # Sort unique x-coordinates to create elementary intervals
        sorted_x = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        m = len(sorted_x) - 1 # Number of elementary intervals
        
        # --- Step 2: Segment Tree Setup ---
        # count[i]: number of active squares fully covering interval i
        # total_len[i]: length of the union of active squares in interval i
        count = [0] * (4 * m)
        total_len = [0.0] * (4 * m)

        def update(node, start, end, l, r, val):
            # If the current node's range is outside the update range
            if r <= start or l >= end:
                return

            # If the current node's range is fully inside the update range
            if l <= start and end <= r:
                count[node] += val
            else:
                mid = (start + end) // 2
                update(2 * node, start, mid, l, r, val)
                update(2 * node + 1, mid, end, l, r, val)
            
            # Update total_len for the current node
            if count[node] > 0:
                # If this node is covered by at least one square, its active length is its full width
                total_len[node] = sorted_x[end] - sorted_x[start]
            else:
                # If not covered, it depends on children (unless it's a leaf)
                if end - start == 1:
                    total_len[node] = 0.0
                else:
                    total_len[node] = total_len[2 * node] + total_len[2 * node + 1]

        # --- Step 3: Create and Sort Y-axis Events ---
        # Event format: (y, type, x_start, x_end)
        # type 1 for bottom edge (add square), -1 for top edge (remove square)
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        # Sort by Y-coordinate
        events.sort(key=lambda x: x[0])
        
        # --- Step 4: Sweep Line Process ---
        total_area = 0.0
        # Store (y_start, height_of_strip, active_width) to find split point later
        strips = [] 
        
        prev_y = events[0][0]
        
        for y, type, x1, x2 in events:
            # Calculate area of the strip between prev_y and current y
            h = y - prev_y
            width = total_len[1] # The root of the tree holds the total active width
            
            if h > 0:
                area = width * h
                total_area += area
                strips.append((prev_y, h, width))
            
            # Update the active x-intervals
            update(1, 0, m, x_map[x1], x_map[x2], type)
            prev_y = y
            
        # --- Step 5: Find the Split Point ---
        target = total_area / 2.0
        current_area = 0.0
        
        for y_start, h, width in strips:
            strip_area = width * h
            if current_area + strip_area >= target:
                # The target line is inside this strip
                needed = target - current_area
                return y_start + (needed / width)
            current_area += strip_area
            
        return float(prev_y)
