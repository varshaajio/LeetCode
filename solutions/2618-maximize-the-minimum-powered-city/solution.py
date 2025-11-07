class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        n = len(stations)
        # prefix sum to compute base power per city
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + stations[i]
        base = [0] * n
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            base[i] = pref[right + 1] - pref[left]

        # checker: can we make every city have at least target power using <= k added stations?
        def can(target):
            diff = [0] * (n + 1)  # diff array for scheduled expirations (exclusive end)
            cur_added = 0
            used = 0
            for i in range(n):
                cur_added += diff[i]  # apply any diff that starts/ends here
                cur_power = base[i] + cur_added
                if cur_power < target:
                    need = target - cur_power
                    used += need
                    if used > k:
                        return False
                    cur_added += need
                    # place at pos = min(n-1, i + r). Its coverage ends at end = min(n-1, pos + r)
                    pos = min(n - 1, i + r)
                    end = min(n - 1, pos + r)
                    # schedule expiration at end+1 (if within bounds)
                    if end + 1 <= n:
                        diff[end + 1] -= need
                # continue to next city
            return True

        # binary search
        lo = 0
        hi = max(base) + k  # upper bound: largest base + all stations
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

