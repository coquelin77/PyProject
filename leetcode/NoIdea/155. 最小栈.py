'''设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.'''
# class MinStack(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         l=[]

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         l.append(x)

#     def pop(self):
#         """
#         :rtype: void
#         """
#         return l.pop(-1)

#     def top(self):
#         """
#         :rtype: int
#         """
#         return l[0]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         for i in l:
#         	if


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.result = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.result.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        else:
            if x < self.min[-1]:
                self.min.append(x)
            else:
                self.min.append(self.min[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.min.pop()
        return self.result.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.result[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
