# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return 0 if root is None else 1 + self.countNodes(root.left) + self.countNodes(root.right)

'''   
     if root == None:
            return 0
        left_height = self.left_h(root)
        right_height = self.right_h(root)

        if left_height == right_height:
            return 2**left_height -1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)



    def left_h(self, node):
        h = 0
        while node:
            h +=1
            node = node.left
        return h
    def right_h(self, node):
        h = 0
        while node:
            h +=1
            node = node.right
        return h
'''
'''
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        no_leaves = self.count_leaves(root)
        height_tree = self.height(root)
        number_of_nodes = self.power_sum(height_tree -2) + no_leaves
        return number_of_nodes

    def count_leaves(self,root):
        if not root:
            return 0
        
        q = deque([root])
        last_level = []
        
        while q:
            level_size = len(q)
            level_nodes = []
            
            for _ in range(level_size):
                node = q.popleft()
                level_nodes.append(node)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            last_level = level_nodes
        
        count = 0
        for node in last_level:
            if not node.left and not node.right:
                count += 1
                
        return count
         
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))
    
    def power_sum(self,n):
        return 2**(n + 1) - 1'''