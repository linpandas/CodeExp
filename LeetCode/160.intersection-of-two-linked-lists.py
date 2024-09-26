#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30204
#
# [160] 相交链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA:
            curA = curA.next
            lenA += 1
        while curB:
            curB = curB.next
            lenB += 1
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        for i in range(lenA-lenB):
            headA = headA.next
        while headA:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None
        
# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

