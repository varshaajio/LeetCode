class Solution(object):
    def reverseVowels(self, s):
        
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s = list(s)  # convert to mutable
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]  # swap vowels
                i += 1
                j -= 1

        return "".join(s)
