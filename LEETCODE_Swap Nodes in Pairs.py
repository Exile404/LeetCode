# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        swapped = ListNode()
        swapped.next = head
        curr = swapped
        while curr.next and curr.next.next:
            x,y = curr.next,curr.next.next
            x.next = y.next
            curr.next = y
            curr.next.next = x
            curr = curr.next.next
        return swapped.next
