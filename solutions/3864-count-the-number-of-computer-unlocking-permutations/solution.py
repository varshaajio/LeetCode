from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        # if complexity[0] is not strictly the global minimum -> impossible
        if any(complexity[i] <= complexity[0] for i in range(1, n)):
            return 0
        # else answer is (n-1)! % MOD
        res = 1
        for k in range(2, n):         # multiply 2 * 3 * ... * (n-1)
            res = (res * k) % MOD
        return res

