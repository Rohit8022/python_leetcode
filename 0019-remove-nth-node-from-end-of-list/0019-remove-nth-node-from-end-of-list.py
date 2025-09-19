# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        '''temp= head
        l=0
        while temp is not None:
            l=l+1
            temp=temp.next
        ele=l-n
        temp=head
        l=0
        if ele==0:
            return temp.next
        while temp is not None:
            l+=1
            if l==ele:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head'''
        dum=ListNode(0,head)
        l=dum
        r=head
        c=0
        while r is not None:
            if c<n:
                r=r.next
                c+=1
            else:
                r=r.next
                l=l.next
        l.next=l.next.next
        return dum.next        






            


