class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        m1=0
        for num in nums:
            if num==1:
                m+=1
                m1=max(m1,m)
            else:
                m=0
            
        return m1         
