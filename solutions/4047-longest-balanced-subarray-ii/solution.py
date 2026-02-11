import sys

# Increase recursion depth to handle the Segment Tree depth for N=10^5
sys.setrecursionlimit(200000)

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        # tree_min and tree_max track the range of balance values in nodes
        # tree_lazy handles the range addition (+1 for evens, -1 for odds)
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        tree_lazy = [0] * (4 * n)
        
        # Initialize tree with large values to represent 'inactive' indices
        def build(v, tl, tr):
            if tl == tr:
                tree_min[v] = tree_max[v] = 10**9
            else:
                tm = (tl + tr) // 2
                build(2*v, tl, tm)
                build(2*v+1, tm+1, tr)
                tree_min[v] = tree_max[v] = 10**9

        def push(v):
            if tree_lazy[v] != 0:
                for child in [2*v, 2*v+1]:
                    tree_lazy[child] += tree_lazy[v]
                    tree_min[child] += tree_lazy[v]
                    tree_max[child] += tree_lazy[v]
                tree_lazy[v] = 0

        def update(v, tl, tr, l, r, add):
            if l > r: return
            if l == tl and r == tr:
                tree_lazy[v] += add
                tree_min[v] += add
                tree_max[v] += add
            else:
                push(v)
                tm = (tl + tr) // 2
                update(2*v, tl, tm, l, min(r, tm), add)
                update(2*v+1, tm+1, tr, max(l, tm+1), r, add)
                tree_min[v] = min(tree_min[2*v], tree_min[2*v+1])
                tree_max[v] = max(tree_max[2*v], tree_max[2*v+1])

        def activate(v, tl, tr, pos):
            if tl == tr:
                tree_min[v] = tree_max[v] = 0
                tree_lazy[v] = 0
            else:
                push(v)
                tm = (tl + tr) // 2
                if pos <= tm: activate(2*v, tl, tm, pos)
                else: activate(2*v+1, tm+1, tr, pos)
                tree_min[v] = min(tree_min[2*v], tree_min[2*v+1])
                tree_max[v] = max(tree_max[2*v], tree_max[2*v+1])

        def find_leftmost_zero(v, tl, tr):
            # If 0 is not in the [min, max] range of this node, skip it
            if tree_min[v] > 0 or tree_max[v] < 0:
                return -1
            if tl == tr:
                return tl
            push(v)
            tm = (tl + tr) // 2
            res = find_leftmost_zero(2*v, tl, tm)
            if res == -1:
                res = find_leftmost_zero(2*v+1, tm+1, tr)
            return res

        build(1, 0, n-1)
        last_pos = {}
        max_ans = 0
        
        for j in range(n):
            # 1. Activate the current starting point 'j' with balance 0
            activate(1, 0, n-1, j)
            
            # 2. Update balance for all subarrays starting after the last occurrence of nums[j]
            x = nums[j]
            p = last_pos.get(x, -1)
            val = 1 if x % 2 == 0 else -1
            update(1, 0, n-1, p + 1, j, val)
            
            last_pos[x] = j
            
            # 3. Find the smallest index i such that the subarray [i...j] is balanced (balance == 0)
            start_idx = find_leftmost_zero(1, 0, n-1)
            if start_idx != -1:
                max_ans = max(max_ans, j - start_idx + 1)
                
        return max_ans
