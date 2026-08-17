class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_count = 0
        
        # Digits that make a number invalid
        invalid_digits = {'3', '4', '7'}
        # Digits that force the number to rotate into a different number
        change_digits = {'2', '5', '6', '9'}
        
        for i in range(1, n + 1):
            s = str(i)
            # Check if any invalid digit exists
            if any(char in invalid_digits for char in s):
                continue
            # Check if at least one changing digit exists
            if any(char in change_digits for char in s):
                good_count += 1
                
        return good_count