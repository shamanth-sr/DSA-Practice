"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque 

class Solution:
    def paths(self, root):
        # code here
        result = []
        current_path = []

        def dfs(node):
            if not node:
                return
            # Add current node to the path
            current_path.append(node.data)

            # If it's a leaf node, append a copy of the path
            if not node.left and not node.right:
                result.append(list(current_path))
            else:
                # Traverse left and right subtrees
                dfs(node.left)
                dfs(node.right)

            # Backtrack
            current_path.pop()

        dfs(root)
        return result