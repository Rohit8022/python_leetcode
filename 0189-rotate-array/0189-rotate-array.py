class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead."""
        #Brutforce
        """
        r=k%len(nums)        
        while r!=0:
            l=nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i]=nums[i-1]
            nums[0]=l
            r-=1  """ 
        nums[:]=nums= nums[len(nums)-k:] + nums[:len(nums)-k]     
