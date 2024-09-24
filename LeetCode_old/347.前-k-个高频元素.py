#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        hashmap = Counter(nums)
        result = []
        for num, freq in hashmap.items():
            heapq.heappush(result, (freq, num))
            if len(result) > k:
                heapq.heappop(result)
        
        return [x[1] for x in result]
# @lc code=end

