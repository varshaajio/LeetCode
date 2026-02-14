class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out=""
        for w in words:
            s=0
            for c in w:
                s+=weights[ord(c)-97]
            out+=chr(122-s%26)
        return out
            
