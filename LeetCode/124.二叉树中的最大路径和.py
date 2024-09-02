#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        self.traversal(root)
        return self.maxSum

    def traversal(self, node):
        if not node:
            return 0
        left = max(self.traversal(node.left), 0)
        right = max(self.traversal(node.right), 0)
        self.maxSum = max(self.maxSum, left + right + node.val)
        return max(left, right) + node.val
# @lc code=end

