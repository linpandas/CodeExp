#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict
        self.preSum = defaultdict(int)
        self.preSum[0] = 1
        return self.traversal(root, 0, targetSum)
    
    def traversal(self, node, curSum, targetSum):
        if not node:
            return 0
        result = 0
        curSum += node.val
        result += self.preSum[curSum-targetSum]
        self.preSum[curSum] += 1
        left = self.traversal(node.left, curSum, targetSum)
        right = self.traversal(node.right, curSum, targetSum)
        result += left + right
        self.preSum[curSum] -= 1
        return result

# @lc code=end

