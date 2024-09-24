#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 与“用最少的箭引爆气球”相比，此处的区间重叠是并，不是交
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(len(intervals)):
            if intervals[i][0] > result[-1][1]: # 注意此处区别
                # 不重叠
                result.append(intervals[i])
            else:
                # 重叠
                result[-1][1] = max(result[-1][1], intervals[i][1])
        
        return result
# @lc code=end



#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#

