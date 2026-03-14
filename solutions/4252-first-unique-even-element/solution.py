class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in nums:
            if i%2==0:
                if nums.count(i)==1:
                    return i
        return -1
        
