# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxD(root.left, 1), self.maxD(root.right, 1))
    def maxD(self, root: Optional[TreeNode], count: int) -> int:
            if not root:
                return count

            count += 1
            
            return max(self.maxD(root.left, count), self.maxD(root.right, count))