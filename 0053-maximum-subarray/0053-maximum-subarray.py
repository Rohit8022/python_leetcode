class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float("-inf")
        maxi=0
        for i in range(len(nums)):
            maxi=nums[i]+maxi 
            ans=max(ans,maxi)
            if maxi<0:
                maxi=0
        return ans        
               

        