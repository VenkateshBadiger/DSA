# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        order = []
        order += self.postorderTraversal(root.left)
        order += self.postorderTraversal(root.right)
        order += [root.val]
        return order