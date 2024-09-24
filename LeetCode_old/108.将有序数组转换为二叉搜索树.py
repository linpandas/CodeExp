#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(nums, 0, len(nums)-1)
    
    def traversal(self, nums, left, right):
        # 左闭右闭区间
        if left > right:
            return
        
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.traversal(nums, left, mid-1)
        node.right = self.traversal(nums, mid+1, right)

        return node
# @lc code=end

