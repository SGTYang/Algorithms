/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    
    ans := head
    
    for head.Next != nil{
        if head.Val == head.Next.Val{
            head.Next = head.Next.Next
        }else{
            head = head.Next
        }
    }
    return ans
}
