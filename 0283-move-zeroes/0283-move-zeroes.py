class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        l=0
        while l<len(nums):
            if nums[l]==0:
                for i in range(l,len(nums)):
                    if i<len(nums)-1:
                        nums[i],nums[i+1]=nums[i+1],nums[i]
                    else:
                        break
                l=l-1         
            l+=1  """
        c=0
        l=0
        while l<len(nums):
            if nums[l]==0:
                nums.pop(l)
                c+=1
                l-=1
            l+=1    
        for i in range(c):          
            nums.append(0)                   

        