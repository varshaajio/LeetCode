import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Helper to check if the array is non-decreasing via violation count
        def get_initial_violations(arr):
            count = 0
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    count += 1
            return count

        vals = list(nums)
        # Doubly linked list simulation
        nxt = [i + 1 for i in range(n)]
        nxt[-1] = -1
        prv = [i - 1 for i in range(n)]
        
        # Track deleted nodes to prevent re-processing
        is_deleted = [False] * n
        
        violations = get_initial_violations(vals)
        if violations == 0:
            return 0

        # Heap stores (sum, left_index, right_index)
        # We include right_index to verify adjacency later
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (vals[i] + vals[i+1], i, i+1))

        ops = 0
        
        while pq:
            s, l, r = heapq.heappop(pq)
            
            # --- STRICT VALIDATION ---
            # 1. Check if l or r were deleted
            # 2. Check if l and r are still immediate neighbors
            # 3. Check if the sum is up-to-date (handles stale heap entries)
            if (is_deleted[l] or is_deleted[r] or 
                nxt[l] != r or 
                vals[l] + vals[r] != s):
                continue
            
            # --- UPDATE VIOLATIONS (Pre-Merge) ---
            # Remove violations involving the old structure of l and r
            if prv[l] != -1 and vals[prv[l]] > vals[l]:
                violations -= 1
            if nxt[r] != -1 and vals[r] > vals[nxt[r]]:
                violations -= 1
            if vals[l] > vals[r]:
                violations -= 1

            # --- EXECUTE MERGE ---
            new_sum = vals[l] + vals[r]
            vals[l] = new_sum
            is_deleted[r] = True  # Mark r as deleted
            
            # Update pointers: l skips over r to the next node
            new_next = nxt[r]
            nxt[l] = new_next
            if new_next != -1:
                prv[new_next] = l

            # --- UPDATE VIOLATIONS (Post-Merge) ---
            # Add violations for the new structure
            if prv[l] != -1 and vals[prv[l]] > vals[l]:
                violations += 1
            if nxt[l] != -1 and vals[l] > vals[nxt[l]]:
                violations += 1
            
            ops += 1
            
            # Check exit condition immediately after valid operation
            if violations == 0:
                return ops

            # --- PUSH NEW NEIGHBORS ---
            # Add new potential pairs to heap. 
            # Note: We do not remove old invalid pairs; the validation step handles them.
            if prv[l] != -1:
                heapq.heappush(pq, (vals[prv[l]] + vals[l], prv[l], l))
            if nxt[l] != -1:
                heapq.heappush(pq, (vals[l] + vals[nxt[l]], l, nxt[l]))

        return ops
