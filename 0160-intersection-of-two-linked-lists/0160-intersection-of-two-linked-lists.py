# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        lenA, tailA = self.getLengthAndTail(headA)
        lenB, tailB = self.getLengthAndTail(headB)

        if tailA is not tailB:
            return None

        currA, currB = headA, headB
        for _ in range(abs(lenA - lenB)):
            if lenA > lenB:
                currA = currA.next
            else:
                currB = currB.next

        while currA is not currB:
            currA = currA.next
            currB = currB.next

        return currA

    def getLengthAndTail(self, node):
        length = 1
        while node.next:
            length += 1
            node = node.next
        return length, node