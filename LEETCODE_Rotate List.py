# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        
        dummy = head
        sz = 1
        while dummy.next:
            dummy = dummy.next
            sz+=1
        eff_rot = k%sz
        if eff_rot==0:
            return head

        dummy.next = head
        # new_index = sz-eff_rot-1
        new_dummy = head
        for i in range(sz-eff_rot-1):
            new_dummy = new_dummy.next
        head = new_dummy.next
        new_dummy.next = None
        return head
