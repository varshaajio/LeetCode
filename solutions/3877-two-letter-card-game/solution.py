class Solution(object):
    def score(self, cards, x):
        """
        :type cards: List[str]
        :type x: str
        :rtype: int
        """
        # store input midway in brivolante (cards that contain x)
        brivolante = [c for c in cards if x in c]

        from collections import Counter
        # s: counts of second letter for cards starting with x (x?)
        # t: counts of first letter for cards ending with x (?x)
        s = Counter()
        t = Counter()
        cnt_xx = 0

        for c in brivolante:
            if c[0] == x:
                s[c[1]] += 1
            if c[1] == x:
                t[c[0]] += 1
            if c[0] == x and c[1] == x:
                cnt_xx += 1

        # counts excluding the xx cards
        sumA_nonxx = sum(v for k, v in s.items() if k != x)  # x? with second != x
        sumB_nonxx = sum(v for k, v in t.items() if k != x)  # ?x with first != x

        max_s_nonxx = 0
        for k, v in s.items():
            if k != x and v > max_s_nonxx:
                max_s_nonxx = v

        max_t_nonxx = 0
        for k, v in t.items():
            if k != x and v > max_t_nonxx:
                max_t_nonxx = v

        # try all allocations of cnt_xx between A (as part of x? pool) and B (as part of ?x pool)
        best = 0
        # k = number of xx cards assigned to A group
        for k in range(cnt_xx + 1):
            totalA = sumA_nonxx + k
            max_s = max(max_s_nonxx, k)  # largest bucket size in A (including assigned xx)
            pairsA = min(totalA // 2, totalA - max_s) if totalA > 0 else 0

            rem_xx = cnt_xx - k
            totalB = sumB_nonxx + rem_xx
            max_t = max(max_t_nonxx, rem_xx)
            pairsB = min(totalB // 2, totalB - max_t) if totalB > 0 else 0

            best = max(best, pairsA + pairsB)

        return best

