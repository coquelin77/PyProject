class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=[];
        i=2
        for i in range(2, n):
           j=2
           for j in range(2,i):
              if(i%j==0):
                 break
           else:
              num.append(i)
        return  len(num)
if __name__ == '__main__':
    a =Solution()
    l=10
    p=a.countPrimes(l)
    print(p)