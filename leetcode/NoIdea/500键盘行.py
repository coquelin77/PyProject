'''给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。



American keyboard



示例：

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]


'''

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lis = []
        s1 = 'qwertyuiopQWERTYUIOP'
        s2 = 'asdfghjklASDFGHJKL'
        s3 = 'zxcvbnmZXCVBNM'

        for i in words:
            if set(i).issubset(s1) or set(i).issubset(s2) or set(i).issubset(s3):
                lis.append(i)

        return lis