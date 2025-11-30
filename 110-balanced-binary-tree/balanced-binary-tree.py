# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        def depth(node: Optional[TreeNode]):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            return 1+ max(left_depth, right_depth)

        if abs(depth(root.left)- depth(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)