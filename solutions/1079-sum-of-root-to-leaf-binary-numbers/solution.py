class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_val):
            if not node:
                return 0
            
            # Step 1: Update the current path value
            # Shift left by 1 and add the current node's bit
            current_val = (current_val << 1) | node.val
            
            # Step 2: If it's a leaf, we've completed one binary number
            if not node.left and not node.right:
                return current_val
            
            # Step 3: Otherwise, continue down the tree and sum the results
            return dfs(node.left, current_val) + dfs(node.right, current_val)
        
        return dfs(root, 0)
