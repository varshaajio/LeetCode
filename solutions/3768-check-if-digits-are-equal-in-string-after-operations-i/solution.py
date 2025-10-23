class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            ns = []
            for i in range(len(s) - 1):
                sm = (int(s[i]) + int(s[i + 1])) % 10
                ns.append(str(sm))
            s = ''.join(ns)
        return s[0]==s[1]

