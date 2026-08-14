class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # Add character to frequency map
            freq[char] = freq.get(char, 0) + 1
            
            # Shrink window if any character exceeds 2 occurrences
            while freq[char] > 2:
                freq[s[left]] -= 1
                left += 1
            
            # Update maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len