#  封装 继承 多态

#  封装

# class aaa():
#
#     pub_res = "公有变量"
#     __pri_res = "私有变量1"
#     _pri_res = "私有变量2"
#
#     def pub_function(self):
#         print("公有方法")
#     def _pri_function(self):
#         print("私有方法1")
#     def __pri_function(self):
#         print("私有方法2")
#
# print(aaa.pub_res)
# print(aaa._pri_res)
# print(aaa().pub_function())
# print(aaa()._pri_function())

#  继承
#
# class Parent():
#
#     money = 10000000000
#     house =  100
#     __yi_wu = "裤子"
#
#     def shou_yi(self):
#         print("点石成金")
#
# class Child(Parent):
#     ai_hao = '花钱'
#     pass
#
# c = Child()
# print(c.ai_hao)
# print(c.money)
# print(c.house)
# print(c.shou_yi())


# class Parent():
#
#     money = 10000000000
#     house =  100
#     __yi_wu = "裤子"
#     def __init__(self,a):
#         self.a = a
#
#     def shou_yi(self):
#         print("点石成金")
#
# p = Parent(123)
# print(p.a)
#
# class Child(Parent):
#     ai_hao = '花钱'
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#
#     # super().  init  (a)
#
#     def shou_yi(self): # 方法重写
#         super().shou_yi()
#        print("影分身之术")
#
#  Child()
# print(c.ai_hao)
# print(c.money)
# print(c.house)
# print(c.shou_yi())

a = 123
b = '456'
#  字符串转数字
print(a + int(b) )
#  数字转字符串
print(str(a) + b)

t = (1,2,3,4)
l = [1,2,3,4,5,65,7]
s = {1,2,3,4,6,9,8}
#  字符串转列表
print(list(b))
#  元组转列表
print(list(t))
#  列表转元组
print(tuple(l))
#  元组转集合
print(set(t))
# 集合转列表
print(list(s))

#  打开模式：r读取 w清空写入 a追加写入 b二进制模式
# f = open("aaa.txt",'a')  # open打开文件
# f.write("\thello") # write写入内容至打开的文件
# print(f.writable()) #  判断是否可写入
# f.close()  # 关闭文件
#
# f = open("aaa.txt",'r')

# print(f.read()) #  默认读取全部数据
# print(f.read(10)) #  读取指定大小的数据
# print(f.readline()) #  按行读取，读取一行
# print(f.readlines()) #  按行读取，读取所有行
# f.close()


a = "abcdefghijklmn"
print(a[0])
print(a[-1])
print(a[1:-2])
print(a[1:-2:2])
print(a[-1:0:-1])
print(a[::-1])
print(a[2:])
print(a[:-2])

a = "abcdefghijklmn"
for i in a:
    print(i)

s = "     aassss     "

print(s.strip())
print(s.lstrip())
print(s.rstrip())

l = "safdsf,sdfsdf,gggg"
print(l.split(","))

with open("aaa.txt",'r') as f: # with 使用一个上下文管理器
    lines = f.readlines()
    print(lines)
    for i in lines:
        print(i.replace("\n",""),end="")  # print 默认带一个换行


s = "sdjfisjif.sfjisjdfi"
print(s.find(".sf"))

# 通过占位符格式化
for i in range(1,10):
    for j in range(1,i+1):
        print("%d x %d = %d"%(j,i,i*j), end="\t")
    print()

# .format
for i in range(1,10):
    for j in range(1,i+1):
        print("{} x {}= {}".format(j,i,i*j), end="\t")
    print()

# print("{:,}".format(1000000000000))
# print("{:^10}".format(123))
# print("{:.2f}".format(2.3467698781))
#
#
#
#
# l = [1,23,2,4,6,7,87]
#
# # l[0] = 20
# # print(l)
# l[1:4] = [20,30,60]
# print(l)
#
# l = [2,3,4,5]
# # l.append("王大锤")
# # l.append("王大锤")
# # l.extend({'123',123})
# l.insert(1,"王大吃哦")
# print(l)
#
# print(l.pop())
# print(l)
#
# print(l.pop(1))
# print(l)
#
# l.remove(3)
# print(l)
#
# l = [2,34,2,5,7,8,2]
# l.remove(2)
# print(1)
#
# l = [True,1,2,5,7,8,2] # python True 1 false 0
# l.remove(1)
# print(l)
#
# l.clear()
# print(l)

a = [5,2,3,6,8,9,123,3,5,7,8123,4]
a.sort()
print(a)
a.sort(reverse=True)
print(a)


d = {"name":"小明","age":18,"sex":"男"}
for key in d:
    print(d[key])

for k,v in d.items():
    print(k,v)

d["addr"] = "上海闵行"
print(d)
d["addr"] = "上海浦东"
print(d)


d = {"name":"小明","age":18,"sex":"男"}
print(d)
d.update({"addr":"上海闵行","学历":"本科"})
print(d)

print(d.pop("addr"))
print(d)

s = {}
for key in d:
    if key == "addr":
        continue
    s[key] = d[key]
print(s)


s = {}
for key in d:
    if key.startswith("a"):
        continue
    s[key] = d[key]
print(s)