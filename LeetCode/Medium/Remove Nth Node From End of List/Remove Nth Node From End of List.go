/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    
    dummyHead := &ListNode{Next: head}
    
    slow, fast := dummyHead, dummyHead
    
    for i:=0; i<=n; i++{
        fast = fast.Next
    }
    
    for fast != nil{
        fast = fast.Next
        slow = slow.Next
    }
    slow.Next = slow.Next.Next
    
    return dummyHead.Next
}
