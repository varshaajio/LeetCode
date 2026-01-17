class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        o=0
        p=set()
        for i in range(len(nums)):
            if not nums[i]==target[i] and not nums[i] in p:
                o=o+1
                p.add(nums[i])
        return o
