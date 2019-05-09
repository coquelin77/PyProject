class Solution():
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #head = [1,1,2]
        if not head:
            return head
        news_ids = []
        for id in head:
            if id not in news_ids:
                news_ids.append(id)
        return news_ids
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #head = [1,1,2]
        
        if not head:
            return head
        
        news_ids = []
        while head:
            id = head.val
            if id not in news_ids:
                news_ids.append(id)
            head = head.next
        return news_ids
'''

if __name__ == '__main__':
    ids = [1,2,2,3]

    a =Solution()
    print(a.deleteDuplicates(ids))