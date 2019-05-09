'''写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]'''


# class Solution:
#     def fizzBuzz(self, n: 'int') -> 'List[str]':
#         list = []
#         for j in range(1, n + 1):
#             list.append(str(j))
#         for i in range(len(list)-1):
#             if int(list[i])%3== 0 and int(list[i])%5!=0:
#                 list[i]=str('Fizz')
#             elif int(list[i])%3!= 0 and int(list[i])%5==0:
#                 list[i]=str('Buzz')
#             elif int(list[i])%3== 0 and int(list[i]%5)==0:
#                 list[i]=str('FizzBuzz')
#             else:
#                 list[i]=str(i)
#         return  list
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

if __name__ == '__main__':
    n=15
    nums=[]
    for i in range(1,n+1):
        nums.append(i)
    a=Solution()
    p=a.fizzBuzz(15)
    print(p)