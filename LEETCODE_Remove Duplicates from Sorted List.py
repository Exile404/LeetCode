# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head
        while current.next:
            if current.val == current.next.val:
                temp = current.next.next
                current.next = temp
            else:
                current = current.next
        
        return head
