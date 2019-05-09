'''编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

 

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        drow = []
        list(s)
        for i in range(0,len(s)-1):
            t=s.pop(-1)
            s.insert(i,t)
        return s


if __name__ == '__main__':
    a = Solution()
    word = ["h", "e", "l", "l", "o"]
    p=a.reverseString(word)
    print(p)
    # word = ["h", "e", "l", "l", "o"]
    # print(type(word))
    # t=word.pop(-1)
    # print(t)
    # print(word)
    # word.insert(0,t)
    # print(word)
    #
    # t = word.pop(-1)
    # print(t)
    # print(word)
    # word.insert(0, t)
    # print(word)
    #
    # t = word.pop(-1)
    # print(t)
    # print(word)
    # word.insert(0, t)
    # print(word)
    #
    # t = word.pop(-1)
    # print(t)
    # print(word)
    # word.insert(0, t)
    # print(word)
    #
    # t = word.pop(-1)
    # print(t)
    # print(word)
    # word.insert(0, t)
    # print(word)