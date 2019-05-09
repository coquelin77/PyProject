class Solution(object):
    def getIntersectionNode(self, headA, headB):
        d = dict()
        while headA:
            d[headA] = 1
            headA = headA.next
        while headB:
            if headB in d:
                return headB
            headB = headB.next
        return None


if __name__ == '__main__':
    intersectVal = 2
    listA = [0, 9, 1, 2, 4]
    listB = [3, 2, 4]
    skipA = 3
    skipB = 1
