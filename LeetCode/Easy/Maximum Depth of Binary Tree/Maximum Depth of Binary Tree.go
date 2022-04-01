/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func Max(a int, b int) int{
    if a>b{
        return a
    }
        return b
}
func maxDepth(root *TreeNode) int {
    var dfs func(head *TreeNode) int
    
    dfs = func(head *TreeNode) int{
        if head == nil{
            return 0
        }
        return Max(dfs(head.Left), dfs(head.Right))+1
    }
    return dfs(root)
}
