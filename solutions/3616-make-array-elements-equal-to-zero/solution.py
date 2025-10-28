class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        valid = 0

        def simulate(start, direction):
            arr = nums[:]  # make a copy to avoid mutation
            curr = start
            dir = direction  # +1 means right, -1 means left
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir *= -1
                    curr += dir
            # after leaving bounds
            return all(x == 0 for x in arr)

        # try all positions where nums[i] == 0
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, -1):  # left
                    valid += 1
                if simulate(i, 1):   # right
                    valid += 1

        return valid

