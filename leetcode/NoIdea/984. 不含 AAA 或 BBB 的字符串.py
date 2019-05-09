class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        a = 'a'
        b = 'b'
        if A < B:
            A, B = B, A
            a, b = b, a
        C = min(A-B, B)
        if C == 0:
            return (a+b)*B
        ans = (2*a+b)*C
        if C == B:
            D = A-2*B
            ans += D*a
            return ans
        else:
            ans += (a+b)*(2*B-A)
            return ans