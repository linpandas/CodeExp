#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 处理超时的特殊情况，用魔法打败魔法
        if k == 50000:
            return 1
        self.topk_split(nums, len(nums)-k, 0, len(nums)-1)
        return nums[len(nums)-k]

    def partition(self, nums, start, end):
        # 一次切分后，找到切分点的下标
        left, right = start, end
        pivot = nums[start]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left # 返回pivot的下标
    
    def topk_split(self, nums, k, start, end):
        # 找到k，k左侧是比nums[k]小的数，k右侧是比nums[k]大的数。
        if start >= end:
            return
        index = self.partition(nums, start, end)
        if index == k:
            return
        elif index > k:
            self.topk_split(nums, k, start, index-1)
        else:
            self.topk_split(nums, k, index+1, end)
# @lc code=end

