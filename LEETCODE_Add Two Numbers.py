class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        res = ListNode(0)
        curr = res
        
        while l1 or l2:
            if l1 is not None:
                dig1 = l1.val
                l1 = l1.next
            else:
                dig1 = 0
            if l2 is not None:
                dig2 = l2.val
                l2 = l2.next
            else:
                dig2 = 0
            summ = carry + dig1 + dig2
            if summ>=10:
                summ -=10
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(summ)
            curr = curr.next
        if carry == 1:
            curr.next = ListNode(1)
        return res.next
