# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                dup_val = cur.next.val
                # 跳过所有值等于 dup_val 的节点
                while cur.next and cur.next.val == dup_val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
