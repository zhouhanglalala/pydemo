# #函数的定义：
# def sigh():
#     print("--------------------")
#     print("  人生苦短，多多加油！ ")
#     print("--------------------")
# #函数的调用
# sigh()
# # --------------------
# #   人生苦短，多多加油！
# # --------------------
# #带参数的函数
# def add(a,b):
#     c=a*b
#     print(c)
#
# add(19,2)

#通过return返回运算结果
# def add(a,b):
#     return a*b
# print(add(12,5))# 返回的结果需要打印
# #返回多个值的函数
# def did(a,b):
#     shang=a/b
#     yushu=a%b
#     return shang,yushu
# print(did(15,3))#(5.0, 0)

# #定义一个函数：
# def line():
#     print("-"*30)
# #定义一条打印n条直线的函数
# def numline(n):
#     i=0
#     while i<n:
#         line()
#         i+=1
#
# numline(5)
#
# #求三个数的和
# def sum(a,b,c):
#     return a+b+c#return仅仅是返回结果，不包含打印的意思
# print(sum(6,6,7))
#
# #完成三个数的平均值计算：
# def avg(a,b,c):
#     return sum(a,b,c)/3#除号是/
# print(avg(3,7,5))

# #局部变量
# def ball():
#     a=1997
#     print("我出生于%s年，我想好好活着。"%a)
#     a=2021
#     print("现在已经%s年，该没有的我还是没有。"%a)
#
# ball()
#
# def bigball():
#     a=2026#不同函数可以定义相同的名字，彼此互不影响。
#     print("不知道在未来的%s年，我是否还是会这样想。"%a)
#
# bigball()
# # "我出生于1997年，我想好好活着。
# # 现在已经2021年，该没有的我还是没有。
# # 不知道在未来的2026年，我是否还是会这样想。"

# #全局变量
# a=2026
# def ball():
#     a=1997
#     print("我出生于%s年，我想好好活着。"%a)
#     a=2021
#     print("现在已经%s年，该没有的我还是没有。"%a)
#
# ball()
#
# def bigball():
#     print("不知道在未来的%s年，我是否还是会这样想。"%a)
#
# bigball()

#在函数中修改全局变量

a=2026
def ball():
    global a
    print("我出生于%s年，我想好好活着。"%a)
    a=2021
    print("现在已经%s年，该没有的我还是没有。"%a)

ball()

def bigball():
    print("不知道在未来的%s年，我是否还是会这样想。"%a)

bigball()
# 我出生于2026年，我想好好活着。
# 现在已经2021年，该没有的我还是没有。
# 不知道在未来的2021年，我是否还是会这样想。
















