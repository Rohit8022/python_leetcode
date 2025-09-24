# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        f=head
        s=head
        while f is not None and f.next is not None:
            s=s.next
            f=f.next.next
        temp=s.next
        s.next=None 
        past=None
        pre=temp
        fet=temp
        while pre is not None:
            fet=pre.next
            pre.next=past
            past=pre
            pre=fet
        temp2=head    
        while temp2 is not None and past is not None:
            sto=temp2.next
            sto2=past.next
            temp2.next=past
            past.next=sto
            temp2=sto
            past=sto2
        return temp2    



        