class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark current 'O' as border-connected ('E')
            board[r][c] = 'E'
            
            # Visit all 4 neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Traversal border cells and mark all connected 'O's as 'E'
        for r in range(rows):
            dfs(r, 0)           # Left border
            dfs(r, cols - 1)    # Right border
            
        for c in range(cols):
            dfs(0, c)           # Top border
            dfs(rows - 1, c)    # Bottom border

        # 2. Final pass: flip 'O' -> 'X' and 'E' -> 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'