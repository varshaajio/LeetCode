class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        
        # Standard Binary Search for Upper Bound
        while low <= high:
            mid = (low + high) // 2
            
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        
        # If low is out of bounds, it means target >= all letters.
        # Using modulo handles the "wrap around" to index 0.
        return letters[low % len(letters)]
