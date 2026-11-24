class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        def fun(i,j1,j2,dp):
            if j1<0 or j2<0 or j1>=c or j2>=c:
                return float('-inf')
            if i==r-1:
                if j1==j2:
                    return grid[i][j1]
                return grid[i][j1]+grid[i][j2]        
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2] 
            maxi=0
            for n_j1 in range(-1,2):
                for n_j2 in range(-1,2):
                    if j1==j2:
                        ans=grid[i][j1]+fun(i+1,j1+n_j1,j2+n_j2,dp)
                    else:
                        ans=grid[i][j1]+grid[i][j2]+fun(i+1,j1+n_j1,j2+n_j2,dp)
                    maxi=max(maxi,ans)
            dp[i][j1][j2]=maxi
            return dp[i][j1][j2]             
                    
        r=len(grid)
        c=len(grid[0])
        dp=[[[-1 for _ in range(c)]for _ in range(c)]for _ in range(r)]
        return fun(0,0,len(grid[0])-1,dp)