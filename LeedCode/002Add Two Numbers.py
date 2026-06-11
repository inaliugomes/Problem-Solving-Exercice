# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(l1:ListNode, l2:ListNode):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        currl1 = l1
        currl2 = l2

        while currl1 is not None:
            print(currl1.val)
            currl1 = currl1.next


addTwoNumbers(l1 = [2,4,3],l2 = [5,6,4])