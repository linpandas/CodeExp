#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 迭代法（中序遍历 + 双指针法）
        stack = []
        pre, cur = None, root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and cur.val <= pre.val:
                    return False
                pre = cur
                cur = cur.right
        return True
    
# class Solution:
#     def __init__(self):
#         self.pre = None
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         # 二叉搜索树的中序遍历是递增的
#         # 递归法（双指针法）
#         if not root:
#             return True
#         left = self.isValidBST(root.left)
#         if self.pre and root.val <= self.pre.val:
#             return False
#         self.pre = root
#         right = self.isValidBST(root.right)

#         return left and right
# @lc code=end

