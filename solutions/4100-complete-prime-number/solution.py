class Solution:
    def completePrime(self, num: int) -> bool:
        s=str(num)
        if not self.isprime(num):
            return False
        for i in range(1,len(s)):
             if not self.isprime(int(s[:i])) or not self.isprime(int(s[i:])):
                return False
        return True
    def isprime(self, num: int)-> bool:
        if num==0 or num==1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
        
