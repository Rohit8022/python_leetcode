class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        pre=matrix[0]
        for i in range(1,n):
            curr=[float("inf")]*n
            for j in range(0,n):
                if j!=0:
                    curr[j-1]=min(curr[j-1],pre[j]+matrix[i][j-1])
                curr[j]=min(curr[j],pre[j]+matrix[i][j])
                if j!=n-1:
                    curr[j+1]=min(curr[j+1],pre[j]+matrix[i][j+1])                        
            pre=curr.copy()
        m=float("inf")
        for i in pre:
            m=min(m,i)
        return m                    

        