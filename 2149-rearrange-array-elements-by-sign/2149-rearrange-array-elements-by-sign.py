class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=0
        r=0
        op=list()
        ch_l=1
        while r<len(nums):
            if ch_l==1 and l<len(nums):
                if nums[l]>0:
                    op.append(nums[l])
                    ch_l=0
                l+=1    
            else:
                if nums[r]<0: 
                    op.append(nums[r])
                    ch_l=1
                r+=1
        #if len(nums)!=len(op):op.append(nums[r])        
        return op           

        