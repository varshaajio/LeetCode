class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        for i in nums:
            if str(digit) in str(i):
                c+=str(i).count(str(digit))
        return c                
        
