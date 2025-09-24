class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q=deque()
        fresh=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c,0))
        ans=0
        while q:
            r,c,t=q.popleft()
            ans=max(ans,t)
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dx,c+dy
                if 0<=nr<R and 0<=nc<C and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc,t+1))
        return ans if fresh==0 else -1