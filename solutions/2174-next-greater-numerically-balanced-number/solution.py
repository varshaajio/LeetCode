from itertools import permutations

class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        balanced_nums = set()
        # digits 1..9 — if we include digit d, it must appear exactly d times
        # try all subsets of digits {1..9} and only keep those with total length <= 7
        for mask in range(1, 1 << 9):
            seq = []
            total_len = 0
            for i in range(9):
                if (mask >> i) & 1:
                    d = i + 1
                    total_len += d
                    if total_len > 7:  # prune: we don't need lengths > 7 for n <= 10^6
                        break
                    seq += [str(d)] * d
            if total_len > 7:
                continue
            # generate all unique permutations for this multiset of digits
            for p in set(permutations(seq)):
                # leading zero can't happen here because seq uses digits 1..9
                num = int(''.join(p))
                balanced_nums.add(num)

        # sort and find smallest > n
        candidates = sorted(balanced_nums)
        for num in candidates:
            if num > n:
                return num

        # Should never reach here for constraints, but safe fallback
        return None

