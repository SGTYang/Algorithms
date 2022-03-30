/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func preorderTraversal(root *TreeNode) []int {
    var (
        ans []int
        recursive func(*TreeNode)
        )
    
    recursive = func(root *TreeNode){
        if root == nil{
            return
        }
        
        ans = append(ans, root.Val)
        recursive(root.Left)
        recursive(root.Right)
    }
    
    recursive(root)
    return ans
}
