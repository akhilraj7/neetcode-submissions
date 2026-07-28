# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Initialize a queue and insert the root node.
        queue = deque([root])

        while queue:
            # Remove the front node
            node = queue.popleft()
            # Swap its left and right children.
            node.left, node.right = node.right, node.left

            # If the left child exists, add it to the queue.
            if node.left:
                queue.append(node.left)
            # If the right child exists, add it to the queue.
            if node.right:
                queue.append(node.right)

        return root
        