class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        repeats = []
        for x in nums:
            if x in seen:
                repeats.append(x)
                # early exit if we already found both (optional)
                if len(repeats) == 2:
                    return repeats
            else:
                seen.add(x)
        return repeats

