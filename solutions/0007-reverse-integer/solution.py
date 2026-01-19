class Solution:
    def reverse(self, x: int) -> int:
        s=1 if x>=0 else -1
        lmt=(2<<30)
        if -lmt <= x < lmt:
            rev=s*int(str(abs(x))[::-1])
            if -lmt <= rev < lmt:
                return rev
            else:
                return 0
        
