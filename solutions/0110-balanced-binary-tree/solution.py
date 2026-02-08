class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Stack stores (node, processed_status)
        stack = [(root, False)]
        # Map to store the height of each node
        depths = {None: 0}
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                # Process the node: check its children's heights
                left_height = depths[node.left]
                right_height = depths[node.right]
                
                # If unbalanced, return False immediately
                if abs(left_height - right_height) > 1:
                    return False
                
                # Store the height of the current node
                depths[node] = 1 + max(left_height, right_height)
            else:
                # Post-order: push node back as visited, then push children
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
                    
        return True
