class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        
        # Step 1: Find the first decreasing digit from the right
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        if i < 0:
            return -1
            
        # Step 2: Find the smallest digit larger than digits[i] to its right
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
            
        # Step 3: Swap them
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the sublist after i to minimize the value
        digits[i + 1:] = reversed(digits[i + 1:])
        
        result = int("".join(digits))
        
        # Step 5: Check 32-bit signed integer limit (2^31 - 1)
        if result > 2**31 - 1:
            return -1
            
        return result