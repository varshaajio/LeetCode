class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total_power = sum(batteries)
        while batteries[-1] * n > total_power:
            n -= 1
            total_power -= batteries.pop()
        return total_power // n
