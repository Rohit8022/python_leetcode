class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        
        '''
        while l<len(nums):
            if r<len(nums)+1:r+=1
            else:l+=1
            if nums[l]+nums[r] == target:
                return l,r'''
        while l<len(nums):
            r=l+1
            while r<len(nums):
                if nums[l]+nums[r] == target: 
                    return l,r
                r+=1
            l+=1               
                


        