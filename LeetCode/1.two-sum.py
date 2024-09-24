# @lcpr-before-debug-begin
from python3problem1 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30204
#
# [1] 两数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [i, hashmap[target - num]]
            else:
                hashmap[num] = i
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

