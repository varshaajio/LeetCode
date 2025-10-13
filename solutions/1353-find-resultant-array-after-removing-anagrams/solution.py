class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        stack = [words[0]]  # start with first word

        for i in range(1, len(words)):
            # Compare sorted forms to detect anagram
            if sorted(words[i]) != sorted(stack[-1]):
                stack.append(words[i])
                
        return stack

