class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                # Isolate the inner string, ignoring the outermost '1' and '0'
                inner = s[i+1:j]
                
                # Recursively process the inner string
                processed_inner = self.makeLargestSpecial(inner)
                
                # Reconstruct the special string and add to our list
                res.append('1' + processed_inner + '0')
                i = j + 1
                
        # Sort the components in descending lexicographical order
        res.sort(reverse=True)
        
        return "".join(res)
