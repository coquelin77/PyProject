'''请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？'''
'''python 快慢指针，反转链表'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True

        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        pre = None
        slow = slow.next
        while slow != None:
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        while pre != None and head != None:
            if pre.val != head.val:
                return False
            else:
                pre = pre.next
                head = head.next
        return True