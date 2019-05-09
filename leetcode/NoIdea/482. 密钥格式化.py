'''给定一个密钥字符串S，只包含字母，数字以及 '-'（破折号）。N 个 '-' 将字符串分成了 N+1 组。给定一个数字 K，重新格式化字符串，除了第一个分组以外，每个分组要包含 K 个字符，第一个分组至少要包含 1 个字符。两个分组之间用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。

给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。

示例 1：

输入：S = "5F3Z-2e-9-w", K = 4

输出："5F3Z-2E9W"

解释：字符串 S 被分成了两个部分，每部分 4 个字符；
     注意，两个额外的破折号需要删掉。
示例 2：

输入：S = "2-5g-3-J", K = 2

输出："2-5G-3J"

解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。'''


class Solution:
    def licenseKeyFormatting(self, S: 'str', K: 'int') -> 'str':
        pass
# python3 先转大写，去破折号，再翻转字符串，每四个字符插入一个破折号，再翻转回来 相同的思路，我写的和别人写的对比：）

# class Solution:
#     def licenseKeyFormatting(self, S, K):
#         """
#         :type S: str
#         :type K: int
#         :rtype: str
#         """
#         S = S.upper()
#         r = ''.join(re.split(r'[^A-Z0-9]', S))
#         l = len(r) // K
#         if len(r) % K == 0:
#             l -= 1
#         r = list(r)[::-1]
#         for i in range(1, l + 1):
#             r.insert(i * (K + 1) - 1,'-')
#         r = ''.join(r)
#         return r[::-1]