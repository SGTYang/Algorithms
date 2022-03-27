/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
    ans := &ListNode{}
    curr := ans
    
    for head != nil{
        if head.Val == val{
            head = head.Next
        }else{
            curr.Next = head
            curr = curr.Next
            head = head.Next
        }
    }
    curr.Next = nil
    return ans.Next
}
