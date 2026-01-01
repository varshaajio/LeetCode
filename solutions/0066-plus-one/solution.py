class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in range(len(digits)):
            num=num*10+digits[i]
        num=num+1
        n=len(str(num))
        n1=10**(n-1)
        d=[]
        while n1>=1:
            d.append(num//n1)
            num=num%n1
            n1//=10
        return d
