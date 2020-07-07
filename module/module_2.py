# from module import module_1
# from module.module_1 import a,name,Test
# from module.module_1 import a as module_1_a,name as module_1_name,Test as module_1_Test

# print(a)
# # print(module_1.a)
# name()
# print(Test.name)

a = "我是模块2中的a变量"

def name():
    print("我是模块2中的name方法")


class Test():
    name("我是模块2中的Test类")


# print(module_1_a)
# # print(module_1.a)
# print(name())
# print(Test.name)

# if __name__ == '__main__':
#     # print(module_1.a)
#     name()
#     print(Test.name)