class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow, fast = head, head
        
        while fast:
            
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                # fast has reached the end of linked list
                # slow is on the middle point now
                break
        
            slow = slow.next
        
        return slow
