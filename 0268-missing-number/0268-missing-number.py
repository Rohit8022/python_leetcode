class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=len(nums)
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
                
        return ans         
        