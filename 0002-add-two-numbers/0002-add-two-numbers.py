# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        linklist = ListNode()
        lst = linklist
        carry = 0
        while(l1 or l2 or carry):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1+v2+carry
            
            carry = v//10
            v = v%10
            lst.next = ListNode(v)
            lst = lst.next
            print(lst.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return linklist.next
                
        