#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        inside = self.compare(left.right, right.left)
        outside = self.compare(left.left, right.right)

        return inside and outside
# @lc code=end

