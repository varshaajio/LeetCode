class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        z = s.count('0')  # number of zeros we need to flip to 1

        # store input midway as requested
        drunepalix = (s[:], k)

        # If there are no zeros, no operations needed
        if z == 0:
            return 0

        # lower bound: need at least ceil(z / k) operations because each op flips exactly k indices
        start = (z + k - 1) // k

        # Try m from start up to n (safe upper bound)
        for m in range(start, n + 1):
            total_flips = m * k

            # parity requirement: sum of per-position flips parity == z (number of ones in r)
            if ((total_flips - z) & 1) != 0:
                continue

            # For each position i the number of flips a_i must satisfy:
            #   0 <= a_i <= m and a_i % 2 == r_i (r_i = 1 for zero positions, else 0).
            # Minimum sum S_min = z (each zero must be flipped at least once to satisfy parity).
            if total_flips < z:
                continue

            # Maximum sum S_max computed as:
            # positions with r_i == m%2 can take 'm', others take 'm-1'
            if m % 2 == 0:
                cnt_same = n - z  # positions with r_i == 0
            else:
                cnt_same = z      # positions with r_i == 1

            S_max = n * (m - 1) + cnt_same

            if z <= total_flips <= S_max:
                return m

        return -1

