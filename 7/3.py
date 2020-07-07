# def shang_yu(a,b):
#     if(b == 0):
#         return None
#     else:
#         return (a//b,a%b)
#
# res = shang_yu(20,0)
# if res is None:
#     print("参数错误")
# else:
#     print("商为：",res[0],"余数为：",res[1])
#
# res = shang_yu(20,10) # 按照位置传参
# if res is None:
#     print("参数错误")
# else:
#     print("商为：",res[0],"余数为：",res[1])
#
# res = shang_yu(b=10,a=20) # 按照关键字传实参
# if res is None:
#     print("参数错误")
# else:
#     print("商为：",res[0],"余数为：",res[1])
#
#
# def sm(a,b=2): # 定义关键字形参，给参数b设置为默认值
#     return a+b
#
# print(sm(2,3))

# c = 1,2,3,4
# a,*b = (1,2,3,4)
#
# print(b)
#
# def sum1(*args):
#     s = 0
#     for i in args:
#         s+=i
#     return s
#
# print(sum1(1,2,3,56))

# def sum1(*args,name="王大锤",**kwargs):
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s+=i
#     return s
#
# print(sum1(name="张三"))
#
# def sum1(name,*args,**kwargs): # *args接收动态位置参数，**kwargs接收动态关键字参数
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s+=i
#     return s
# print(sum1(name="张三"))

# class calc():
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc()  # 类的实例化 c对象
#
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()
#
#
# class calc():
#     res=None
#
#     def __init__(self,a,b): #  魔法函数，类实例化的时候调用，又称构造方法
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc(29,39)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()


 # 九九乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",i*j,end="\t")
#     print()


l = [2,6,89,56,77,256,87,66]

length = len(l)
for i in range(length-1,0,-1): #  外层循环确定排好序的数据下标
    for j in range(i):  #  遍历未排好序的列表
        if (l[j] > l[j+1]):  #  判断相邻两个数据,前边的如果大于后边的,则交换两个数据的位置
            l[j],l[j+1] = l[j+1],l[j]
print(l)