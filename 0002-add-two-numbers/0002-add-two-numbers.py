# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''val1=0
        val2=0
        t1=l1
        t2=l2
        while t1 is not None or t2 is not None:
            if t1 is not None:
                val1=(val1*10+t1.val)
                t1=t1.next
            if t2 is not None:
                val2=(val2*10+t2.val)
                t2=t2.next
        ans=val1+val2
        l=ListNode()
        if ans==0:
            return ListNode(0)
        t3=l
        val1=0
        while ans!=0:
            t3.next=ListNode(ans%10,None)
            t3=t3.next
            ans=ans//10
        return l.next   '''
       
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next




            
        