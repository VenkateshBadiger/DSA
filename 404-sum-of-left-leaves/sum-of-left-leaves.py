# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], flag: bool = False) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return root.val if flag else 0
        
        left_sum = self.sumOfLeftLeaves(root.left,True)
        right_sum = self.sumOfLeftLeaves(root.right,False)
        return left_sum + right_sum
