# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy= tmp = ListNode()
        carrier = 0
        
        while l1 or l2 or carrier != 0:
          
            number_sum = 0
            
            if l1:
                number_sum += l1.val
                l1 = l1.next
            if l2:
                number_sum += l2.val
                l2 = l2.next
            number_sum += carrier
            carrier = number_sum//10
            node = ListNode(number_sum%10)
            tmp.next = node
            tmp = tmp.next
        
        return dummy.next
