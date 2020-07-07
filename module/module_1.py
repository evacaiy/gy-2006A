from module.module_2 import a as module_2_a

#  from import语句会把要导入的模块执行一遍之后再导入当前模块

a = "我是模块1中的a变量"

def name():
    print("我是模块1中的name方法")


class Test():
    name = "我是模块1中的Test类"


print(module_2_a)