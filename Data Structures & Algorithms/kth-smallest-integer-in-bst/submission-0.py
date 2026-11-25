class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal count, ans
            if not node or ans is not None:
                return

            # Visit left subtree first for ascending order in a BST
            inorder(node.left)

            # Process current node and stop once we hit the kth smallest
            count += 1
            if count == k:
                ans = node.val
                return

            inorder(node.right)

        inorder(root)
        return ans