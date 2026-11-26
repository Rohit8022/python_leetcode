class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s=0
        s+= sum(nums)
        sm=int(s/2)
        if s % 2 != 0:
            return False                
        dp=[[False for _ in range(sm+1)]for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=True
        if nums[0]<=sm:    
            dp[0][nums[0]]=True
        for i in range(1,len(nums)):
            for t in range(sm+1):
                if nums[i]>t:
                    pic=dp[i-1][t]
                else:
                    pic=dp[i-1][t-nums[i]]
                npic=dp[i-1][t]
                dp[i][t]=pic or npic
        return dp[len(nums)-1][sm]            

        