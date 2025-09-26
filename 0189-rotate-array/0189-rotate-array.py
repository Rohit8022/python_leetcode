class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
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
        # WORK ONLY IN PYTHON
        """    
        r=k%len(nums)    
        nums[:]=nums= nums[len(nums)-r:] + nums[:len(nums)-r] """
        # INTERVIEW PREFFERD SOLUTION(SAME FOR ALL LANGUAGE) 
        l=len(nums)
        reverse(l-k,l-1)
        reverse(0,l-k-1)
        reverse(0,l-1)
        



