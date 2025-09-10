# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        dummy = ListNode()
        cur = dummy
        carry = 0
        while head1 and head2:
            carry, digit = divmod(head1.val + head2.val +carry, 10)
            cur.next = ListNode(digit)
            cur = cur.next
            head1 = head1.next
            head2 = head2.next

        while head1:
            carry, digit = divmod(head1.val + carry, 10)
            cur.next = ListNode(digit)
            cur = cur.next
            head1 = head1.next

        while head2:
            carry, digit = divmod(head2.val + carry, 10)
            cur.next = ListNode(digit)
            cur = cur.next
            head2 = head2.next

        if carry:
            cur.next = ListNode(carry)

        return dummy.next
