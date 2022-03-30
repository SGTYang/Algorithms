/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    ans := []int{}
    
    var recursive func(head *TreeNode)
    
    recursive = func(head *TreeNode){
        if head == nil{
            return
        }
        recursive(head.Left)
        ans = append(ans, head.Val)
        recursive(head.Right)
    }
    recursive(root)
    return ans
}
