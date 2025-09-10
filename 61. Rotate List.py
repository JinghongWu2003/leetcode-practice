# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k < 1:
            return head
        dummy = ListNode(0, head)
        length = 0
        cur = dummy
        while cur.next:
            length += 1
            cur = cur.next

        if length == 1:
            return head
        move = k % length

        if move == 0:
            return head

        first = dummy.next
        cur = dummy
        for _ in range(length - move):
            cur = cur.next
        end = cur
        dummy.next = cur.next
        for _ in range(move):
            cur = cur.next
        cur.next = first
        end.next = None
        return dummy.next



