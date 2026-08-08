class Solution(object):
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]
        
        # If the starting pixel already has the target color, no fill is needed
        if original_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Check matrix boundaries and matching color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            
            # Recolor current pixel
            image[r][c] = color
            
            # Explore 4 directional neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image