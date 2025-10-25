class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        days = n % 7
        total = 0
        total += weeks * 28
        # Add the increment for each week: additional dollars for each week, sum of arithmetic progression
        total += 7 * (weeks * (weeks - 1)) // 2

        # Remaining days in the last (possibly incomplete) week
        for i in range(days):
            total += weeks + i + 1

        return total

