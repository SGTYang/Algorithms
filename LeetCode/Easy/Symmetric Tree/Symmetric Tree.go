/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    
    var recursive func(head1 *TreeNode, head2 *TreeNode) bool
    
    recursive = func(head1 *TreeNode, head2 *TreeNode) bool{
        if head1==nil && head2==nil{
            return true
        }
        if (head1==nil || head2==nil) || head1.Val != head2.Val  {
            return false
        }
        return recursive(head1.Left,head2.Right) && recursive(head1.Right, head2.Left)
    }
    return recursive(root.Left, root.Right)
}
