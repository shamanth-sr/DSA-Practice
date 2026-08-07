# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []

        maxWidth = 0
        
        queue = deque()
        queue.append((root, 0))

        while queue:
            size = len(queue)
            minIndex = queue[0][1]

            firstIndex = 0
            lastIndex = 0

            for i in range(size):
                node, index = queue.popleft()
                currIndex = index - minIndex

                if i == 0:
                    first = currIndex
                if i == size - 1:
                    last = currIndex

                if node.left:
                    queue.append((node.left, 2 * currIndex + 1))
                if node.right:
                    queue.append((node.right, 2 * currIndex + 2))

            maxWidth = max(maxWidth, last-first+1)
        return maxWidth


                       