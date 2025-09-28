# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        list3=ListNode()
        temp3=list3
        
        while temp1 is not None and temp2 is not None:
            if temp1.val<=temp2.val:
                temp3.next=temp1
                temp1=temp1.next
            else:
                temp3.next=temp2
                temp2=temp2.next     
            temp3=temp3.next
        if temp1 is not None:
            temp3.next=temp1 
        if temp2 is not None:
            temp3.next=temp2              
        return list3.next        

        