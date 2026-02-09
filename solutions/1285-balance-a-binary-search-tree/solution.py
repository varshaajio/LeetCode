class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Extract values in sorted order
        sorted_values = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_values.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        # Step 2: Build a balanced BST from the sorted list
        def build_balanced_tree(left, right):
            if left > right:
                return None
            
            # Pick the middle element to ensure balance
            mid = (left + right) // 2
            node = TreeNode(sorted_values[mid])
            
            # Recursively build left and right subtrees
            node.left = build_balanced_tree(left, mid - 1)
            node.right = build_balanced_tree(mid + 1, right)
            
            return node
            
        return build_balanced_tree(0, len(sorted_values) - 1)
