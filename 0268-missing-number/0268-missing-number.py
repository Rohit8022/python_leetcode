class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #TIME COMPLEXITY = O(n log n)
        """
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
                
        return len(nums)
        l=0
        while l<len(nums)"""
        #TIME COMPLEXITY = O(n) 
        #SPACE COMPLEXITY = O(n)
        freq=[]
        for i in range(len(nums)+1):
            freq.append(-1) 
        for i in range(len(nums)):
            freq[nums[i]]=nums[i]
        for i in range(len(freq)):
            if freq[i]==-1:
                return i    


                      
        