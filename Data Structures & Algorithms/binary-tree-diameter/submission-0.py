# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0

        def maxDepth(root):
            nonlocal diameter


            # If node doesn't exist
            if root is None:
                return 0

            # Calculate left subtree height
            left = maxDepth(root.left)

            # Calculate right subtree height
            right = maxDepth(root.right)
            diameter=max(diameter,left+right)

            # Return maximum height + current node
            return 1 + max(left, right)

        maxDepth(root)
        return diameter
            