class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert integer to string for easy digit iteration
        s = str(n)
        
        # Count frequencies of digits
        freq = [0] * 10  # freq[i] = frequency of digit i
        for ch in s:
            freq[int(ch)] += 1
        
        # Find the least frequent digit (excluding digits not present at all)
        min_freq = float("inf")
        ans = -1
        for d in range(10):
            if freq[d] > 0:  # only consider digits present in n
                if freq[d] < min_freq:
                    min_freq = freq[d]
                    ans = d
        
        return ans

