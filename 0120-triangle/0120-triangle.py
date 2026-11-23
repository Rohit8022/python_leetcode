class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        pre=[0]
        pre=triangle[0]
        for i in range(1,n):
            curr=[0]*(i+1)
            for j in range(0,i+1):
                if j==0:
                    curr[j]=pre[j]+triangle[i][j]
                    continue
                if j==i:
                    curr[j]=pre[j-1]+triangle[i][j]
                    continue
                curr[j]=min(pre[j-1]+triangle[i][j],pre[j]+triangle[i][j])
            pre=curr.copy()
        m=pre[0]        
        for i in pre:
            m=min(m,i)
        return m    




        