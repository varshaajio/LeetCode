from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        curr = 1
        idx = 0  # pointer in target
        
        while idx < len(target):
            if curr == target[idx]:
                result.append("Push")
                idx += 1
            else:
                result.append("Push")
                result.append("Pop")
            curr += 1
        
        return result

