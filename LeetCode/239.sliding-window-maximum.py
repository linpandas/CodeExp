#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30204
#
# [239] 滑动窗口最大值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        result = []
        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        result.append(queue[0])

        for i in range(k, len(nums)):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])

            if nums[i-k] == queue[0]:
                queue.popleft()
            result.append(queue[0])
        
        return result
# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

