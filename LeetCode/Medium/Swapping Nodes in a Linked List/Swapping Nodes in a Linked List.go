/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func swapNodes(head *ListNode, k int) *ListNode {
    buffer, cur := make([]*ListNode, 0), head
    
    for cur != nil{
        
        buffer = append(buffer, cur)
        cur = cur.Next    
        
    }
    buffer[k-1].Val, buffer[len(buffer)-k].Val = buffer[len(buffer)-k].Val, buffer[k-1].Val
    
    return buffer[0]
}
