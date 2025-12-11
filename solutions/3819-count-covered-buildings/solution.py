from typing import List
import collections

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # row_min[x], row_max[x] = smallest and largest y in row x
        # col_min[y], col_max[y] = smallest and largest x in column y
        row_min = collections.defaultdict(lambda: 10**9)
        row_max = collections.defaultdict(lambda: -1)
        col_min = collections.defaultdict(lambda: 10**9)
        col_max = collections.defaultdict(lambda: -1)

        for x, y in buildings:
            if y < row_min[x]: row_min[x] = y
            if y > row_max[x]: row_max[x] = y
            if x < col_min[y]: col_min[y] = x
            if x > col_max[y]: col_max[y] = x

        covered = 0
        for x, y in buildings:
            if row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]:
                covered += 1

        return covered

