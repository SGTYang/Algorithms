/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func trimBST(root *TreeNode, low int, high int) *TreeNode {
    
    var recursive func(head *TreeNode, low, high int) *TreeNode
    
    recursive = func(head *TreeNode, low, high int) *TreeNode{
        if head == nil{
        return nil
        }
        if head.Val < low{
            return recursive(head.Right,low,high)
        }else if head.Val > high{
            return recursive(head.Left,low,high)
        }else{
            head.Left = recursive(head.Left,low,high)
            head.Right = recursive(head.Right,low,high)
            return head
        }
    }
    return recursive(root,low,high)
}
