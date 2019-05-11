class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #如果n大于0而且是偶数
        if(n>0 and n%2==0):
            while(n>2):
                n=n/2
                if(n==2):
                    return True
            return False
        elif(n==1):
            return True
        else:
            return False

if __name__ == '__main__':
    num = 5
    a= Solution()
    if(a.isPowerOfTwo(n=num)==0):
        print('False')
    else:
        print('True')