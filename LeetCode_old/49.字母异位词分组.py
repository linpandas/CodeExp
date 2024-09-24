#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hashmap = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            hashmap[key].append(s)
        
        return list(hashmap.values())
# @lc code=end

