# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_kth(self, cur: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 从 cur 出发向后走 k 步，若能走到则返回该节点；否则返回 None
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1) 找到这一组的尾结点 kth（从 group_prev 之后走 k 步）
            kth = self.get_kth(group_prev, k)
            if not kth:  # 不足 k 个，结束
                break
            group_next = kth.next

            # 2) 在区间 [group_prev.next, kth] 内原地反转，尾部指向 group_next
            prev = group_next
            cur = group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            # 现在 prev == kth，是这一组反转后的新头

            # 3) 三段接回去，并推进 group_prev
            tmp = group_prev.next        # 反转前的组头（现在是新尾）
            group_prev.next = kth        # 上一段连到新头
            group_prev = tmp             # 新尾成为下一轮的 group_prev

        return dummy.next
