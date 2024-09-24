#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        counts = Counter()
        countp = Counter(p)
        result = []
        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            while counts[s[r]] > countp[s[r]]:
                counts[s[l]] -= 1
                l += 1
            if r - l + 1 == len(p):
                result.append(l)
        
        return result

# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

