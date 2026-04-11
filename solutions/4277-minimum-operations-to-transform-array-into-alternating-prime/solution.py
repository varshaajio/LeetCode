class Solution:
    def minOperations(self, nums: list[int]) -> int:
        c=0
        for i in range(len(nums)):
            n=nums[i]
            c1=n
            if i%2==0:
                while not self.isprime(c1):
                    c1+=1
                c+=c1-n
            else:
                c1=n
                while self.isprime(c1):
                    c1+=1
                c+=c1-n
        return c      
    def isprime(self,n):
        if n<2:
            return False
        if n<4:
            return True
        if n%2==0 or n%3==0:
            return False
        i=5
        while i*i<=n:
            if n%i==0 or n%(i+2)==0:
                return False
            i+=6
        return True
