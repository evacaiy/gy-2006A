# a = 1
# b = 10
# print(a+b)
#
#
#
# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)
#
# x,y,*z = (1,2,3,4,5)
# print(x)
# print(y)
# print(z)
#
# a = 10
# b = 20
# print(a+b)
# print(a-b)
# print(a*b)
# print(b/a)
# print(b % a)
# print(3**3)
# print(a//b)
#
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
#
# print(a and b)
# print(a or b)
#
# x = 1,2,3,4,5
# print(1 in x)
# print(1 not in x)
#
# z = 11
# print(z % 2 == 0)
#
# z = 12331
# print(z %  10)
# z //= 10
# print(z)
#
# print(z%10)
#
# l = ("果芽","老干妈","腾讯","百度","阿里")
# if ("果芽" in l):
#     print("合作方")
# else:
#     print("非合作方")
#
# score = 50
# if (score < 0):
#     print("请输入正确的成绩")
# if (score > 0 and score < 60):
#     print("不及格")
# if (score >= 60 and score <= 70):
#     print("及格")
# if (score >= 71 and score <= 80):
#     print("良好")
# if (score >=81 and score <= 100):
#     print("优秀")
# if (score > 100):
#     print("请输入正确的成绩")
#
#
# score = 60
# if (score > 0 and score < 60):
#     print("不及格")
# elif (score >= 60 and score <= 70):
#     print("及格")
# elif (score >= 71 and score <= 80):
#     print("良好")
# elif (score >=81 and score <= 100):
#     print("优秀")
# else:
#     print("请输入正确的成绩")
#
#
# score_1 = [98,55,60,23,45,56,85,79,91,92,100,86,77,96,43]
# for score in score_1:
#     if (score > 0 and score < 60):
#          print("不及格")
#     elif (score >= 60 and score <= 70):
#          print("及格")
#     elif (score >= 71 and score <= 80):
#          print("良好")
#     elif (score >=81 and score <= 100):
#          print("优秀")
#     else:
#          print("请输入正确的成绩")
#
#
# # 100以内数的和 不算100
# s = 0
# for i in range(100):
#     s = s + i
# print(s)
#
# # range()
# # 第一个参数：起始数据 默认为0
# # 第二个参数：代表结束值，不包含边界
# # 第三个参数：步长（增量） 默认值为1
#
# for i in range(1,100,2):
#     print(i)
#
# for i in range(100,0,-1):
#     print(i)
#
#
# # 求出10*9*8...*1 的结果 10的阶乘 10！
# s = 1
# for i in range(10,0,-1):
#     s = s * i
# print(s)
#

# 猜数字

# flag = True
# a = 62
#
# while flag:
#     b = int(input("请输入数字"))
#     if b > a:
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         flag = False

# #  找出100以内可以被3整除的数字
# for i in range(1,100):
#     if (i % 3 != 0):
#         continue
#     print(i)

#  定义一个求两个数商和余数的方法

# a = 20
# b = 10
# print(a % b)
# print(a // b)

# def level(a,b):
#     print(a % b)
#     print(a // b)
# level(20,10)
# level(5,3)

# def div(a,b):
#     print(a % b)
#     print(a // b)
# div(20,10)
# div(5,3)

# #  定义一个求两个数商和余数的方法
# def shang_yu(a,b): # a,b形参
#     print("商:",a // b,",余数:",a % b)
#
# shang_yu(10,5) #方法调用 10，5实参
# shang_yu(20,3)

# def shang_yu(a,b):
#     if(b==0):
#         return None
#     else:
#         return (a//b,a%b)
# shang_yu(20,3)

res = shang_yu (20,0)

if res is None:
    print("参数错误")
else:
    print("商为:",res[0],",余数为:",res[1])


