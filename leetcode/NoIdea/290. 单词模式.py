# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
#
# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 示例 4:
#
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
class Solution:

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ")

        if len(pattern) != len(str_list): return False

        if len(set(pattern)) != len(set(str_list)): return False

        for i in range(1, len(str_list)):
            if pattern[i] == pattern[i - 1]:
                if str_list[i] == str_list[i - 1]:
                    pass
                else:
                    return False

            else:
                if str_list[i] == str_list[i - 1]:
                    return False
                else:
                    pass
        return True
if __name__ == '__main__':
    mode="abba"
    word="dog cat cat dog"
    a=Solution()
    p=a.wordPattern(mode,word)
    print(p)