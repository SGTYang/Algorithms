/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func convertBST(root *TreeNode) *TreeNode {
    var sum int
    var recursive func(head *TreeNode) *TreeNode
    
    recursive = func(head *TreeNode) *TreeNode{
        if head == nil{
            return nil
        }
        recursive(head.Right)
        head.Val += sum
        sum = head.Val
        recursive(head.Left)
        return head
    }
    
    return recursive(root)
}
