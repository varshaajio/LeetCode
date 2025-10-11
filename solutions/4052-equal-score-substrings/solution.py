class Solution(object):
    def scoreBalance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tot=0
        for char in s:
            tot+=ord(char)-ord('a')+1
        p=0
        for i in range(len(s)-1):
            p+=ord(s[i])-ord('a')+1
            if p+p==tot:
                return True
        else:
            return False
