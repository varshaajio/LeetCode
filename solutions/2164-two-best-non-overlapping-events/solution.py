from bisect import bisect_left
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort by start time
        events.sort()
        n = len(events)

        # suffixMax[i] = max value from i to end
        suffixMax = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], events[i][2])

        starts = [e[0] for e in events]
        ans = 0

        for i in range(n):
            s, e, v = events[i]
            # take only this event
            ans = max(ans, v)

            # find next event that starts after current ends
            j = bisect_left(starts, e + 1)
            if j < n:
                ans = max(ans, v + suffixMax[j])

        return ans

