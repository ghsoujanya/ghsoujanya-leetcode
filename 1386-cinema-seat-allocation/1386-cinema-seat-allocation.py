from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map row -> bitmask of reserved seats from index 2 to 9
        seats = defaultdict(int)
        
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                # Set the bit corresponding to (col - 2)
                seats[row] |= (1 << (col - 2))
                
        # Bitmasks for 4-seat blocks (seats 2-5, 6-9, 4-7)
        left_mask   = 0b00001111  # seats 2, 3, 4, 5
        right_mask  = 0b11110000  # seats 6, 7, 8, 9
        middle_mask = 0b00111100  # seats 4, 5, 6, 7
        
        # Completely empty rows can seat 2 families each
        ans = (n - len(seats)) * 2
        
        for mask in seats.values():
            left_open = (mask & left_mask) == 0
            right_open = (mask & right_mask) == 0
            
            if left_open and right_open:
                ans += 2
            elif left_open or right_open or (mask & middle_mask) == 0:
                ans += 1
                
        return ans