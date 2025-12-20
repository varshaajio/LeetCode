from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Mark each number's corresponding index as negative
        for num in nums:
            index = abs(num) - 1  # map number to index
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # All positive indices +1 are missing numbers
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result

