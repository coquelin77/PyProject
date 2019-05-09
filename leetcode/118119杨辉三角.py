class Solution:
    def triangles(self):  # 杨辉三角
        L = [1]
        while True:
            yield L
            L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
            L.insert(0, 1)
            L.append(1)


    def generate(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        n = 0
        results = []
        for t in self.triangles():

            if n == rowIndex:
                return results
            print(t)
            results.append(t)
            n = n + 1
if __name__ == '__main__':
    a = Solution()
    a.generate(4)
# class Solution:
#     def getRow(self, rowIndex):
#         """
#         :type rowIndex: int
#         :rtype: List[int]
#         """
#         res = [1, 1]
#         if rowIndex == 0:
#             return [1]
#         if rowIndex == 1:
#             return res
#         for i in range(2, rowIndex+1):
#             tmp = [1]
#             for j in range(i-1):
#                 tmp.append(res[j] + res[j+1])
#             tmp.append(1)
#             res = tmp
#         return res
#
# if __name__ == '__main__':
#     a= Solution()
#     p=a.getRow(23)
#     print(p)