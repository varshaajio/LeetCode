class Solution(object):
    def magicalSum(self, m, k, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute factorials and inv factorials up to m
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (m + 1)
        invfact[m] = pow(fact[m], MOD-2, MOD)
        for i in range(m, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD

        # Precompute pow(nums[i], c) for c=0..m
        pow_num = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for c in range(1, m+1):
                pow_num[i][c] = pow_num[i][c-1] * (nums[i] % MOD) % MOD

        # DP dimensions:
        # dp[carry][ones][t] = value (sum of prod(nums[i]^c_i / c_i!) over assignments for processed positions)
        # We'll keep ones only up to k (prune >k).
        # carry ranges 0..m
        max_carry = m
        # Choose number of positions to iterate: up to n + enough to flush carry. m<=30, so n+30 is safe.
        max_pos = n + 30

        # initialize
        dp_cur = [ [ [0] * (m+1) for _ in range(k+1) ] for _ in range(max_carry+1) ]
        dp_cur[0][0][0] = 1

        for pos in range(max_pos):
            dp_next = [ [ [0] * (m+1) for _ in range(k+1) ] for _ in range(max_carry+1) ]
            # for pos < n we have choices c=0..m with weight pow_num[pos][c]*invfact[c]
            # for pos >= n only c=0
            if pos < n:
                for carry in range(max_carry+1):
                    for ones in range(k+1):
                        row = dp_cur[carry][ones]
                        # skip if all zeros
                        # iterate t only where row[t]!=0
                        for t in range(m+1):
                            base_val = row[t]
                            if base_val == 0:
                                continue
                            # choose c from 0..m-t (can't exceed remaining picks)
                            max_c = m - t
                            for c in range(max_c+1):
                                total = c + carry
                                bit = total & 1
                                new_ones = ones + bit
                                if new_ones > k:
                                    continue
                                new_carry = total >> 1
                                add = base_val * pow_num[pos][c] % MOD * invfact[c] % MOD
                                dp_next[new_carry][new_ones][t + c] = (dp_next[new_carry][new_ones][t + c] + add) % MOD
            else:
                # only c=0
                for carry in range(max_carry+1):
                    for ones in range(k+1):
                        row = dp_cur[carry][ones]
                        for t in range(m+1):
                            base_val = row[t]
                            if base_val == 0:
                                continue
                            total = carry  # c=0
                            bit = total & 1
                            new_ones = ones + bit
                            if new_ones > k:
                                continue
                            new_carry = total >> 1
                            dp_next[new_carry][new_ones][t] = (dp_next[new_carry][new_ones][t] + base_val) % MOD

            dp_cur = dp_next

        # result: carry must be 0, ones=k, t=m
        res = dp_cur[0][k][m] * fact[m] % MOD
        return res

