# 语法检查
# a = 100
# print(b)  # 语法错误
# b = 20  # 语法错误

# f = open("bbbb.txt",'r')  # 异常
# print(f.read())
# f.close()


# try:
#     f = open("bbbb.txt",'r')  # 异常
#     print(f.read())
#     f.close()
# except:
#     print("文件不存在")
#
#
# print("操作完文件")

#
# def div(a,b):
#     try:
#         return a / b
#     except:
#         return
#
# print(div(10,0))

class CustomException(Exception):
    def __init__(self,value="值不能为0"):
        self.value = value

    def __str__(self):
        return self.value

a = 0
try:
    if a == 0:
        print("a = {} 触发异常".format(a))
        raise   CustomException
    print("a={} 未触发异常".format(a))
except CustomException as e:
    print(e)

