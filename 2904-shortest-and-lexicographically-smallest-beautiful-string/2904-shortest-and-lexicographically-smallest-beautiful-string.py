class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Collect indices of all '1's in the string s
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        # If there are fewer than k ones, no valid substring exists
        if len(ones) < k:
            return ""
        
        ans = ""
        
        # Iterate over all valid sliding windows containing exactly k ones
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            
            # Update ans if it's the first match, shorter, or lexicographically smaller
            if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                ans = sub
                
        return ans