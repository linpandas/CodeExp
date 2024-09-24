#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxL = 0
        self.traversal(root)
        return self.maxL

    def traversal(self, node):
        if not node:
            return 0
        left = self.traversal(node.left)
        right = self.traversal(node.right)
        self.maxL = max(self.maxL, left + right)

        return max(left, right) + 1
# @lc code=end

