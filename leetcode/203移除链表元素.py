'''删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return head

        while (head):
            if head.val == val:
                head = head.next
                continue
            break

        if not head:
            return head

        prev = head
        node = head.next

        while (node):
            if node.val == val:
                if node.next:
                    prev.next = node.next
                    node = node.next
                    continue
                else:
                    prev.next = None
                    break
            prev = node
            node = node.next

        return head