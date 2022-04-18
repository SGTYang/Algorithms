/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func traverse(node *TreeNode, k *int, res *int) {
    if node == nil {
        return
    }
    traverse(node.Left, k, res)
    
    *k--
    if *k == 0 {
        *res = node.Val
        return
    }
    
    traverse(node.Right, k, res)
}

func kthSmallest(root *TreeNode, k int) int {
    var res int
    traverse(root, &k, &res)
    return res
}
