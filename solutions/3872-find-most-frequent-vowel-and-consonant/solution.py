class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=dict()
        vowel,cons={0},{0}
        for c in s:
            d[c]=d.get(c,0)+1
            if c in 'aeiou':
                vowel.add(d[c])
            else:
                cons.add(d[c])
        return max(vowel)+max(cons)

            
