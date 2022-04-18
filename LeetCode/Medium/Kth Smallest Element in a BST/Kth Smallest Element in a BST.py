# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = self.res = 0
        def recursive(node):
            if not node:
                return
            
            recursive(node.left)
            self.cnt +=1
            if self.cnt == k:
                self.res = node.val
                return
            recursive(node.right)
            
        recursive(root)
        
        return self.res
