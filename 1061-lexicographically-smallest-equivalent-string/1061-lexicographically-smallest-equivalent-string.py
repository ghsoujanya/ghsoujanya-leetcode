class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize parent array where each character (0-25) is its own parent initially
        parent = list(range(26))
        
        def find(i: int) -> int:
            if parent[i] == i:
                return i
            # Path compression: update parent[i] to point directly to the root
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i: int, j: int):
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                # Always attach the larger character's root to the smaller character's root
                if root_i < root_j:
                    parent[root_j] = root_i
                else:
                    parent[root_i] = root_j

        # Union characters from s1 and s2 that are at the same index
        for char1, char2 in zip(s1, s2):
            union(ord(char1) - ord('a'), ord(char2) - ord('a'))
            
        # Map each character in baseStr to its lexicographically smallest equivalent
        res = []
        for char in baseStr:
            smallest_char_idx = find(ord(char) - ord('a'))
            res.append(chr(smallest_char_idx + ord('a')))
            
        return "".join(res)