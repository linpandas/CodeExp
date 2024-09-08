#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = dict()
        for i, c in enumerate(s):
            last_occurrence[c] = i
        
        result = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])
            if i == end:
                result.append(end-start+1)
                start = end + 1
        
        return result
# @lc code=end

