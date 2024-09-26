#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30204
#
# [35] 搜索插入位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <target:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

