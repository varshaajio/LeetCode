class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        # Quick impossible cases: any factor 2 or 5 -> no repunit divisible
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        for length in range(1, k + 1):          # at most k steps needed
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        return -1

