'''颠倒给定的 32 位无符号整数的二进制位。

 

示例 1：

输入: 00000010100101000001111010011100
输出: 00111001011110000010100101000000
解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
示例 2：

输入：11111111111111111111111111111101
输出：10111111111111111111111111111111
解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
      因此返回 3221225471 其二进制表示形式为 10101111110010110010011101101001。'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        def b_to_d(i):
            result = 0
            a = 1
            while i > 0:
                result += (i % 10) * a
                a *= 2
                i = i // 10
            return result

        def d_to_b(i):
            result = []
            a = 1
            while i > 0:
                result.append(str(i % 2))
                i = i // 2
            if len(result) < 32:
                result += ['0'] * (32 - len(result))
            return ''.join(result)

        n = d_to_b(n)
        n = int(n)
        n = b_to_d(n)
        return n
if __name__ == '__main__':
    a= Solution()
    bit = '11111111111111111111111111111101'
    p=a.reverseBits(bit)
    print(p)