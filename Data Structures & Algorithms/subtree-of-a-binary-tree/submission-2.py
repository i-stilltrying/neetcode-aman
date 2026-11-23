# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            
        def isSameTree(p,q):
            # 1. Both nodes are None: identical empty branches
            if not p and not q:
                return True

            # 2. One node is None or values differ: mismatch found
            if not p or not q or p.val != q.val:
                return False

            # 3. Recursively verify both left and right subtrees match
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not subRoot:
            return True
        if not root:
            return False


        if isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            