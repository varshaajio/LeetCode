class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # We iterate from the end of the string to the second character (index 1)
        # We stop at index 0 because the problem ends when the number is "1"
        for i in range(len(s) - 1, 0, -1):
            digit = int(s[i]) + carry
            
            if digit == 1:
                # The number is odd (either it was 1 + 0 carry, or 0 + 1 carry)
                # 1 step to add 1, 1 step to divide by 2
                steps += 2
                carry = 1
            else:
                # digit is 0 (0 + 0 carry) or 2 (1 + 1 carry)
                # In both cases, the result of the operation is even
                # 1 step to divide by 2
                steps += 1
                # If digit was 2, carry remains 1; if 0, carry remains 0
                # This is simplified by: if digit was 2, we already have carry=1
        
        # Finally, check the leftmost bit (s[0]) with the carry
        return steps + carry
