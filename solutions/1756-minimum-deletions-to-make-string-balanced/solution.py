class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        # Brute Force Step 1: Pre-calculate the 'b' count on the left for EVERY index
        left_b = [0] * (n + 1)
        b_count = 0
        for i in range(n):
            left_b[i] = b_count
            if s[i] == 'b':
                b_count += 1
        left_b[n] = b_count # Total b's

        # Brute Force Step 2: Pre-calculate the 'a' count on the right for EVERY index
        right_a = [0] * (n + 1)
        a_count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                a_count += 1
            right_a[i] = a_count
            
        # Brute Force Step 3: Now iterate through every single point in the string
        # and "brutely" check the sum of deletions needed at that split.
        min_deletions = n
        for i in range(n + 1):
            current_cost = left_b[i] + right_a[i]
            if current_cost < min_deletions:
                min_deletions = current_cost
                
        return min_deletions
