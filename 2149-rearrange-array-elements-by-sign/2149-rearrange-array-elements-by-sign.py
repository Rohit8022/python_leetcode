class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #MY APPROCH
        '''
        l=0
        r=0
        op=list()
        ch_l=1#CHECK FLAG 1=WILL RUN/0=WILL NOT
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
        return op
        '''
        #CODE AND DEBUG
        op=[0]*len(nums)
        pos=0
        neg=1
        for i in range(len(nums)):
            if nums[i]>0:
                op[pos]=nums[i]
                pos+=2
            else:
                op[neg]=nums[i]
                neg+=2
        return op            


        