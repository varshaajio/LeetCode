class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type blLetters: str
        :rtype: int
        """
        count = 0
        words=text.split()
        for ch in words:
            found = True
            for c in brokenLetters:
                if c in ch:
                    found = False
                    break
            if found:
                count += 1
        return count
