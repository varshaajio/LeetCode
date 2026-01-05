class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            s1=1+i
            c=2
            for j in range(2,int(i**0.5)+1):
                if c<=4:
                    if i%j==0:
                        if j!=i//j:
                            s1+=j+i//j
                            c+=2
                        else:
                            s1+=j
                            c+=1
                else:
                    break
            if c==4:
                s+=s1
        return s
