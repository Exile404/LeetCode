
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        level = 1
        max_sum = root.val
        max_level = 1
        while queue:
            summ = 0
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                summ+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if summ>max_sum:
                max_sum = summ
                max_level = level
            level+=1
        return max_level
      
