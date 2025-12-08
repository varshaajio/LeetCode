class Solution:
    def countTriples(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                s=(i*i+j*j)**0.5
                if s.is_integer() and s<=n:
                    c+=1
        return c
