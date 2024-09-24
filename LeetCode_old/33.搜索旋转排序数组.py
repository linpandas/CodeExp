#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 两段二分，先找到最小值下标->找到l,r->二分搜索
        i = self.findMin(nums) # 最小值的下标
        if target > nums[-1]:
            l, r = 0, i - 1
        else:
            l, r = i, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[l] == target:
            return l
        return -1

    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        return l
# @lc code=end

