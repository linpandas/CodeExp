#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         # 递归遍历
#         if not root:
#             return []
#         left = self.preorderTraversal(root.left)
#         right = self.preorderTraversal(root.right)

#         return [root.val] + left + right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 迭代遍历
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            # 栈先进后出，前序遍历（中左右），为了让left先弹出，需要先把right加入栈里
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result


# @lc code=end

