# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       
        result = []
        level = 0
        node = root

        def rightView(node, level):
            if node == None:
                return
            if level == len(result):
                result.append(node.val)
            rightView(node.right, level + 1)
            rightView(node.left, level + 1)

        rightView(node, level)
        return result

        