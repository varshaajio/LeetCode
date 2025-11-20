class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # sort by end ascending; if same end, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = 0
        # keep last two chosen points (a < b). initialize to very small
        a = -10**18
        b = -10**18

        for l, r in intervals:
            if l > b:
                # neither a nor b in [l,r], pick r-1 and r
                ans += 2
                a, b = r - 1, r
            elif l > a:
                # only b is in [l,r], pick r
                ans += 1
                a, b = b, r
            else:
                # both a and b already in [l,r], do nothing
                pass

        return ans

