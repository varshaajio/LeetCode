class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def isPalindrome(n:int)-> bool:
            if str(n)==str(n)[::-1]:
                return True
            else:
                return False
        
        out=[]
        for i in range(len(nums)):
            n=0
            while True:
                l=nums[i]+n
                h=nums[i]-n
                lb=int(bin(l)[2:])
                hb=int(bin(h)[2:])
                if isPalindrome(lb) or ((hb > 1) and isPalindrome(hb)):
                    out.append(n)
                    break
                n+=1
        return out
            
