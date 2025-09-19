class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs( i,j, k):
            if k==len(word):
                return True
            if not(0<=i<rows and 0<=j<cols) or board[i][j]!=word[k]:
                return False
            tmp, board[i][j]=board[i][j],"#"
            found=(
                dfs(i+1,j,k+1) or
                dfs(i-1,j,k+1) or
                dfs(i,j+1,k+1) or
                dfs(i,j-1,k+1)
            )
            board[i][j]=tmp
            return found
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True

        return False