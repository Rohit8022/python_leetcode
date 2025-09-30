class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #TIME COMPLEXITY = O(n2)
        '''
        l=0
        while l<len(nums):
            r=l+1
            while r<len(nums):
                if nums[l]+nums[r] == target: 
                    return l,r
                r+=1
            l+=1
        '''
        #TIME COMPLEXITY = O(n) 
        #SPACE COMPLEXITY = O(n)
        d={}
        for i in range(len(nums)):
            rem =target-nums[i]
            if rem in d:
                return d[rem],i 
            d[nums[i]]=i        

                


        