class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''l=0
        ans=0
        while l< len(prices):
            r=l+1
            while r<len(prices):
                ans1=prices[r]-prices[l]
                ans=max(ans,ans1)
                r+=1
            l+=1
        return ans ''' 
        ma=0
        mi=float("inf")
        for i in range(len(prices)):
            mi=min(mi,prices[i])
            if prices[i]>mi:
                ma=max(ma,(prices[i]-mi))
        return ma        




        