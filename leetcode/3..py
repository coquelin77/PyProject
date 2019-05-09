class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__list = []
        self.__state = []
        self.__min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.__list.append(x)
        if len(self.__list) == 1:
            min = x
            self.__state.append(x)
        else:
            if x < self.__state[-1]:
                self.__state.append(x)
            else:
                pass
        return 'DONE'

    def pop(self):
        """
        :rtype: None
        """
        if len(self.__list) == 1:
            t = self.__list.pop(-1)
            
            del self.__state[-1]
            return t

    def top(self):
        """
        :rtype: int
        """
        return self.__list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.__state[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
