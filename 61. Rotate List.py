# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1) 统计长度并定位尾结点
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # 2) 规范化 k
        k %= n
        if k == 0:
            return head

        # 3) 连成环：tail -> head
        tail.next = head

        # 4) 走 n-k-1 步到新尾，新头是 new_tail.next
        steps = n - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 5) 断开环
        new_tail.next = None
        return new_head
