#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start

## 将元组视为栈中元素，栈中元素为(当前的值val，栈内最小值)
class MinStack:
    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if not self.items:
            self.items.append((val, val))
        else:
            self.items.append((val, min(val, self.items[-1][1])))

    def pop(self) -> None:
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

