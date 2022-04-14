/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
    var recursive func(head *TreeNode, val int) *TreeNode

    recursive = func(head *TreeNode, val int) *TreeNode{
        if head == nil{
            return nil
        }
        if head.Val == val{
            return head
        }else if head.Val < val{
            return recursive(head.Right,val)
        }else{
            return recursive(head.Left,val)
        }
        return nil
    }
    return recursive(root,val)
}
