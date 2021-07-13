# 维护两个栈，第一个栈支持插入操作，第二个栈支持删除操作

class CQueue:
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def appendTail(self, value: int) -> None:
        self.stack_a.append(value)  # 压入

    def deleteHead(self) -> int:
        if not self.stack_a:  # 栈a中没有元素，返回 -1
            return -1
        if self.stack_b:  # 栈b中有元素，直接返回栈b的栈顶
            return self.stack_b.pop()  # 返回栈顶元素
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
