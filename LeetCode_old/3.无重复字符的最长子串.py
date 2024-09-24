#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxL = 0, 0
        for r, c in enumerate(s):
            while c in s[l:r]:
                l += 1
            maxL = max(maxL, r-l+1)
        return maxL
# @lc code=end

