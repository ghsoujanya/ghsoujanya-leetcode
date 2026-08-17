class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        for _ in range(4):
            # Check if current matrix equals target
            if mat == target:
                return True
            
            # Rotate matrix 90 degrees clockwise
            mat = [[mat[n - 1 - c][r] for c in range(n)] for r in range(n)]
            
        return False