"""
file: 437_Path Sum
about:
author: Xiaohong Liu
date: 30/04/20
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0

        path_in_root = self.count(root, sum)
        path_in_left = self.pathSum(root.left, sum)
        path_in_right = self.pathSum(root.right, sum)

        return path_in_root + path_in_left + path_in_right

    def count(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        num_in_root = 1 if root.val == sum else 0
        num_in_left = self.count(root.left, sum - root.val)
        num_in_right = self.count(root.right, sum - root.val)

        return num_in_root + num_in_left + num_in_right