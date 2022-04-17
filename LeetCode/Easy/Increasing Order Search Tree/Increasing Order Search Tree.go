/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func increasingBST(root *TreeNode) *TreeNode {
    var recursive func(head *TreeNode)
    ans := &TreeNode{}
    prev := ans

    recursive = func(head *TreeNode) {
        if head == nil{
            return 
        }
        recursive(head.Left)
        prev.Right = head
        prev = head
        prev.Left = nil
        recursive(head.Right)

        return
    }
    recursive(root)
    return ans.Right
}
