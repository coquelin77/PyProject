class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        result = 1
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                if i != num/i:
                    result += i + num/i
                else:
                    result += i
        return result == num