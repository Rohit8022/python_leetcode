class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        def fun(m,n,dp):
            if m < 0 or n < 0:
                return 0
            if obstacleGrid[m][n] == 1:
                return 0
            if m == 0 and n == 0:
                if obstacleGrid[0][0]==1:
                    return 0
                return 1
            if dp[m][n] != -1:
                return dp[m][n]            
            up=fun(m-1,n,dp)
            do=fun(m,n-1,dp) 
            dp[m][n]=up+do
            return dp[m][n]   
                  
        m=len(obstacleGrid)-1
        n=len(obstacleGrid[0])-1
        dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]  
        return fun(m,n,dp)      

        