# class MyStack(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.list = []
#
#     def push(self, x):
#         """
#         Push element x onto stack.
#         :type x: int
#         :rtype: void
#         """
#         self.list.append(x)
#
#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         :rtype: int
#         """
#         if len(self.list) == 0:
#             return
#         else:
#             e = self.list[-1]
#             del self.list[-1]
#             return e
#
#     def top(self):
#         """
#         Get the top element.
#         :rtype: int
#         """
#         if len(self.list) == 0:
#             return
#         else:
#             t = self.list[-1]
#             return t
#
#     def empty(self):
#         """
#         Returns whether the stack is empty.
#         :rtype: bool
#         """
#         if len(self.list) == 0:
#             return True
#         else:
#             return False
#
#
# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()
# if __name__ == '__main__':
#     a = MyStack()
#     x = 2
#     y = 3
#     z = 4
#     a.push(x)
#     a.push(y)
#     a.push(z)
#     print(a.pop())
#     print(a.top())
#     print(a.empty())
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__queue=[]
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.__queue)==0:
            self.__queue.append(x)
        else:
            self.__queue.append(x)
            for i in range(0,len(self.__queue)-1):
                # tmp = self.__queue[0]

                self.__queue.append(self.__queue.pop(0))
                i+=1
        return 'DONE'
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # t = self.__queue[0]
        # del self.__queue[0]
        return self.__queue.pop(0)
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.__queue[0]
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.__queue)==0:
            return True
        else:
            return False
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
if __name__ == '__main__':
    a = MyStack()
    x = 2
    y = 3
    z = 4
    a.push(x)
    a.push(y)
    a.push(z)
    print(a.pop())
    print(a.top())
    print(a.empty())