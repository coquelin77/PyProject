
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = numerator//denominator#地板除
        ex = numerator%denominator
        # lr = list(result)
        # for i in range(1,len(lr)):
        #     if lr[i]==lr[i-1]:
        #        pass
        return result,ex

if __name__ == '__main__':
    numerator = 6
    denominator = 2
    #输出: "0.5"
    a = Solution()
    p=a.fractionToDecimal(numerator,denominator)
    print(p)