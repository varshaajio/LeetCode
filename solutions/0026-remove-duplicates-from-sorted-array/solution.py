class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0  # slow pointer
        for j in range(1, len(nums)):  # fast pointer
            if nums[j] != nums[i]:   # found a new unique element
                i += 1
                nums[i] = nums[j]    # place it next in line

        return i + 1   # length of unique elements

