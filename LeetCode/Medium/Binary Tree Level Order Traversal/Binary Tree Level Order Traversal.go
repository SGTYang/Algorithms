/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    if root == nil{
        return nil
    }
    que := make([]*TreeNode, 1)
    level := 0
    var ans [][]int
    que[0] = root
    
    for len(que) > 0{
        currlen := len(que)
        for i:=0; i<currlen; i++{
            node := que[0]
            que = que[1:]
            if len(ans) == level{
                ans = append(ans, []int{node.Val})
            }else{
                ans[level] = append(ans[level],node.Val)
            }
            if node.Left != nil{
                que = append(que, node.Left)
            }
            if node.Right != nil{
                que = append(que, node.Right)
            }
        }
        level ++
    }
    return ans
}
