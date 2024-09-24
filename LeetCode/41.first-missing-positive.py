#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            # 将所有负数和超过len(nums)的数都赶走
            if  num < 0 or num > len(nums):
                nums[i] = 0
        for i, num in enumerate(nums):
            # 跳过空座位和坐对的人
            if num == 0 or num == i + 1:
                continue
            nums[i] = 0 # 坐错了，赶走并置零
            while num != nums[num-1]:
                # 是空座位，直接坐
                if nums[num-1] == 0:
                    nums[num-1] = num
                else:
                    # 让坐错的人离开，num左上，并将坐错的人视为新的num
                    nums[num-1], num = num, nums[num-1]
        if 0 in nums:
            return 1 + nums.index(0) # nums[i] == 0, 返回i+1
        return 1 + len(nums)
# @lc code=end



#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

