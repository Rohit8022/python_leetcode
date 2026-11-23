class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        pre=[0]*c
        pre[0]=grid[0][0]
        for i in range(1,c):
            pre[i]=pre[i-1]+grid[0][i]
        for i in range(1,r):
            curr=[0]*c
            for j in range(c):
                if j==0:
                    curr[j]=pre[j]+grid[i][j]
                    continue 
                curr[j]=min(curr[j-1]+grid[i][j],pre[j]+grid[i][j])
            pre=curr.copy()
        return pre[c-1]           
        