# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.max_product = 0

        # Step 1: compute total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        # Step 2: compute subtree sums and maximize product
        def subtreeSum(node):
            if not node:
                return 0
            
            left = subtreeSum(node.left)
            right = subtreeSum(node.right)
            curr_sum = node.val + left + right

            # product if we cut above this subtree
            self.max_product = max(
                self.max_product,
                curr_sum * (total - curr_sum)
            )

            return curr_sum

        subtreeSum(root)

        return self.max_product % MOD

