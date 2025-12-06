class Solution:
    def sumNumbers(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            # Form the number so far
            current = current * 10 + node.val
            
            # If it's a leaf -> return the formed number
            if not node.left and not node.right:
                return current
            
            # Otherwise sum left + right
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)
