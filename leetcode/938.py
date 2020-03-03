# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

# The binary search tree is guaranteed to have unique values.

def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    if not root:
        return 0
    elif root.val < L:
        return self.rangeSumBST(root.right, L, R)
    elif root.val > R:
        return self.rangeSumBST(root.left, L, R)
    return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)