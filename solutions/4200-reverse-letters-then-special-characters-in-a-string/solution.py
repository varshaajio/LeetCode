class Solution:
    def reverseByType(self, s: str) -> str:
        l=[]
        sc=[]
        for c in s:
            if c in "!@#$%^&*()":
                sc.append(c)
            else:
                l.append(c)
        l.reverse()
        sc.reverse()
        r=""
        a=0
        b=0
        for c in s:
            if c in "!@#$%^&*()":
                r=r+sc[a]
                a+=1
            else:
                r=r+l[b]
                b+=1
        return r
                
            
        
                
