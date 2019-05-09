# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return
        else:
            before = head
            after = head.next

            while after:
                if after.val == before.val:
                    after = after.next
                    before.next = after
                else:
                    next = pre.next
                    after = after.next


if __name__ == '__main__':
    l = [1, 1, 2]
    pre, cur = head, head.next
    while cur:
        if cur.val == pre.val:
            cur = cur.next
            pre.next = cur
        else:
            pre = pre.next
            cur = cur.next
    return head


class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return
        else:
            before = head
            after = head.next

            while after:
                if after.val == before.val:
                    after = after.next
                    before.next = after
                else:
                    before = before.next
                    after = after.next
            return head

