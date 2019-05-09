'''编写一个程序，从键盘输入圆的半径r，圆柱的高h，分别计算出圆周长出来，圆面积cs和圆柱的体积cv
输出结果时保留小数点后4位'''

#
# class V(object):
#     def baidu(self,r,h):
#         #r = int(input("圆的半径是?"))
#         #h = int(input("圆柱的高是?"))
#         s = r * r * 3.14
#         # 圆柱的表面积=侧面积+两个底面积=2πrh+2πr^2
#         cs = (2 * 3.14 * r * h) + (2 * 3.14 * r) * (2 * 3.14 * r)
#         cv = 3.14 * r * r * h
#         #round(s,5)
#         s = ("%.4f" % s)
#         cs = ("%.4f" % cs)
#         cv = ("%.4f" % cv)
#         zhouchang = "圆的周长是"+str(s)
#         mianji="圆柱的面积是"+str(cs)
#         tiji = "圆柱的体积是"+str(cv)
#         return  zhouchang,mianji,tiji
# if __name__ == '__main__':
#     r = float(input("圆的半径是?"))
#     h = float(input("圆柱的高是?"))
#     a=V()
#     p=a.baidu(r,h)
#     print(p)

'''求100-200之间的素数，按每行10个输出，要求在奇数中找素数 '''


# class V(object):
#     def baudu(self, start, end):
#         sushu = []
#         for i in range(start, end + 1):
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             if i == j + 1:
#                 sushu.append(i)
#         ten = []
#         for p in range(1, len(sushu)):
#             ten.append(sushu[p])
#             if p % 10 == 0:
#                 print(ten)
#                 ten = []
#
#         return 'DONE!'
#
#
# if __name__ == '__main__':
#     # ！/usr/bin/python
#     # -*- coding:UTF-8 -*-
#     # 求素数
#     kaishi = 100
#     jieshu = 200
#     nums = V()
#     print(nums.baudu(start=kaishi, end=jieshu))
