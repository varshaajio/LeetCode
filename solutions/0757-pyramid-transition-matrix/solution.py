from collections import defaultdict
from functools import lru_cache

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Build mapping: (left, right) -> list of possible tops
        trans = defaultdict(list)
        for a, b, c in allowed:
            trans[(a, b)].append(c)

        @lru_cache(None)
        def dfs(row: str) -> bool:
            # If we've reached the top
            if len(row) == 1:
                return True

            # Generate all possible next rows
            def build_next(i: int, current: str) -> bool:
                if i == len(row) - 1:
                    return dfs(current)

                pair = (row[i], row[i + 1])
                if pair not in trans:
                    return False

                for ch in trans[pair]:
                    if build_next(i + 1, current + ch):
                        return True
                return False

            return build_next(0, "")

        return dfs(bottom)

