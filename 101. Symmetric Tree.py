"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            clone = Node(cur.val)
            clone.next = cur.next
            cur.next = clone
            cur = clone.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        pseudo = Node(0)
        copy_cur = pseudo
        cur = head
        while cur:
            clone = cur.next
            nxt = clone.next

            copy_cur.next = clone
            copy_cur = clone

            cur.next = nxt
            cur = nxt
        return pseudo.next