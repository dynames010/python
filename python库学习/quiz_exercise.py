#参考答案：https://baijiahao.baidu.com/s?id=1693899920928313921&wfr=spider&for=pc

'''
1、一行代码实现1--100之和
'''
import copy
import time
import random
import re
# #方法一 sum函数
# print(sum(range(100)))
# #方法二 reduce函数，可以完成迭代
# #reduce函数的使用
# from functools import reduce
# def add(x,y):
#     return x+y
# sum = reduce(add,range(100))
# print(sum)
# #方法三 自定义函数lambda
# sum2 = reduce(lambda a,b: a+b,range(100))
# print(sum2)
#
# '''扩展'''
# #自定义函数的定义和使用规则
# #*代表的含义可变长参数（位置参数），参数会收集在元组中;在函数调用时*也可用于拆解元组为位置参数
# def change_para (*tp1): # 注：后续的参数必须以关键词参数方式提供,否则会提示报错
#     print(type(tp1))
#     print(tp1)
# change_para("1","2","3")
# chara = (4,5,6)
# change_para(*chara)
# #**代表以字典方式收集到变量之中；在函数调用时，会拆解字典作为关键字参数
# def cube_test (**nature):
#     all_nature = {'dog':8}
#     all_nature.update(nature)
#     print(nature)
# dic_para = {'dog':3,'cat':4}
# cube_test(dog=1,cat=2)  #函数名关键字参数的用法，参数变量名=参数值，故key值不需要加引号
# cube_test(**dic_para)
# #字典定义,有三种方式
# dic_list = [('name','dog'),('sex','f'),('gendre','f')]  #列表元组转换为字典
# add2_dic = dict(dic_list)
# dic_usr = {'name':1,'sex':2}    #直接定义
# add_dic = dict(money=0,age=30)   #dic函数
# print(dic_usr)
# print(add_dic)
# print(add2_dic)


'''
2、如何在一个函数内部修改全局变量
'''
# #函数中添加global关键字，global可以把一个变量变为全局变量
# cat = 1
# dog = 2
# def test_sum():
#     global dog
#     dog = 3
#     print('tmp is {0}'.format(dog))
#     return cat + dog
# test_sum()
# print(dog)


'''
3、列出5个python标准库
'''
#os\time\sys\abc\re\string\random\shutil

'''
4、字典如何删除键和合并两个字典
'''
# dic1 = {'name':'dog','age':16,'weight':70}
# dic2 = {'hobby':'swim'}
# #删除 方法一
# dic1.pop('name')
# print('delete result is {0}'.format(dic1))
# #删除 方法二
# del dic1['age']
# print('del dic is {0}'.format(dic1))
# #删除 方法三
#print(i) for i in range(10) if True
# res = {key:value for key,value in dic1.items() if key!='age'}
# print(res)
# #update函数
# dic1.update(dic2)
# print('update result is {0}'.format(dic1))

# 5、谈下python的GIL
#
'''
6、python实现列表去重的方法
'''
#错误的
# list = [1,2,2,3,4,8,1]
# print(list)
# print(len(list))
# for i in range(0,len(list)):
#     print('i={0}'.format(i))
#     for j in range(0,len(list)):
#         print('j={0}'.format(j))
#         if list[i]==list[j]:
#             list.pop(j)
#             break
#     print(list)
# print(list)
# #方法一 set函数
# list = [1,2,3,4,4,5]
# lst = set(list)
# print(lst)
#
# #方法二 count函数
# list = [i for i in list if list.count(i)==1]
# print(list)

'''
7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
'''
# #*args位置参数,接收的实际是一个tuple元组,表示接收参数的数目,**kwargs关键字参数,接收的是一个字典
# def fun(*args,**kwargs):
#     print('{0},{1}'.format(args[0],args[1]))
#     print('{0},{1}'.format(kwargs['name'],kwargs['your']))
# fun(1,2,3,'a',name = 'dog',your = 'cat')

'''
8、python2和python3的range（100）的区别
'''
#python3中返回的是可迭代对象，python2中返回的是一整个列表加载到内存中



'''
9、一句话解释什么样的语言能够用装饰器?
'''
#装饰器好处，相同的代码不重复写；能够包装一个函数或类，缩减代码量
#能够实现闭包的语言，即如果在外函数中定义了一个内函数，内函数中引用了外函数的临时变量，并且外函数的返回值是对内函数的引用
#函数能够作为传递到的对象

# def calculate_time(func):
#     def inner(x):
#         t1 = time.time()
#         func(x)
#         t2 = time.time()
#         t3 = t2 - t1
#         print(t3)
#     return inner
#
# @calculate_time
# def add(x):
#     print('try')
# add(1)

'''
10、python内建数据类型有哪些
'''
#数字
#序列对象：字符串、列表、元组
#字典
#文件
#集合 set方法，集合是无序的

'''
11、简述面向对象中__new__和__init__区别
'''
#__init__是在创建对象之后，初始化函数的一些变量；__new__在__init__之前操作,__new__(cls)，虽然有cls但是静态方法，需要传入的类名

'''
12、简述with方法打开处理文件帮我我们做了什么？
'''
#单独的f.open方法会出现异常状况，需要写异常判断try except finally，with帮助我们进行了异常判断，不断何种情况都会进行f.close关闭文件


'''
13、python中生成随机整数、随机小数、0--1之间小数方法
'''
# list = ['dog','cat','fish','c']
# #0-1之间生成浮点数
# print('random 0-1 is :{0}'.format(random.random()))
# #生成指定范围内的整数
# print('point 1,100 is {0}'.format(random.randint(1,100)))
# #生成随机的浮点数
# print('random float is {0}'.format(random.uniform(0,10)))
# #从序列中获取随机元素
# print('random string is {0}'.format(random.choice(list)))

'''
14、避免转义给字符串加哪个字母表示原始字符串？
'''
#添加\\，字符串前添加r

'''
15、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
'''
#
# string = '<div class="nam">中国</div>'
# rule = re.compile('<div class=(.*)>(.*?)</div>')
# result = re.search(rule,string).group(2)
# print(result)

'''
16、python中断言方法举例
'''
# #断言成功则继续执行，断言失败则抛出异常
# assert (1>0)
# print('yes')
# assert (0>1)
# print('no')

# 17、python2和python3区别？列举5个
#https://zhuanlan.zhihu.com/p/34751635/

'''
18、列出python中可变数据类型和不可变数据类型，并简述原理
'''
#可变数据类型：列表、字典
#不可变数据类型：元组、字符串

'''
19、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
'''
#注：sorted方法返回值是none
# s = "ajldjlajfdljfddd"
# y = set(s)
# print(y)
# y = list(y)
# print(y)
# y.sort(reverse=False)
# print(y)
# res = "".join(y)
# print(res)

'''
20、用lambda函数实现两个数相乘
'''
#拓展
#lambda好处：精简代码，省去定义函数，一般配合filter()map()函数使用
#map()函数
# def square(x):
#     return x*x
# a= [i for i in map(square,[1,2,3,4,5])]
# print(a)
# sum = lambda x,y:x*y
# tmp = (lambda a:a+1)(3) #括号中直接传递值使用
# print(tmp)
# print(sum(2,5))


'''
21、字典根据键从小到大排序
'''
#
# dic = {'d':10,'a':8,'t':12,'m':9}
# key_list = []
# for key,value in dic.items():
#     key_list.append(key)
# key_list.sort()
# by_key = sorted(dic.items(),key = lambda item:item[0],reverse=True)
# print(by_key)
# print(dict(by_key))

'''
22、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
'''
# 对dict\list\set和tuple更高效的操作
# from collections import Counter
# list = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# result = Counter(list)
# result.subtract('l')
# result_list3 = Counter(list).most_common(3)
#
# print(result)
# print(result_list3)

'''
# 23、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出 "张三  深圳"
'''
# #
# import re
# #方法一：中文匹配
# a = "not 404 found 张三 99 深圳"
# chinese = re.compile('[\u4e00-\u9fa5]+')
# word_list = re.findall(chinese,a)
# print('  '.join(word_list))
# #方法二：re.sub过滤
# a = "not 404 found 张三 99 深圳"
# print(a.split())
# S = re.sub(r"[0-9a-zA-Z]",'',a).split()
# print(S)

'''
# 24、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
#
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def judge_single(x):
#     if x%2!=0:
#         return x
# print(list(filter(judge_single,a)))

'''
# 25、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
#列表推导式，把循环结果放在列表中,可以嵌套for循环或者其他循环结果，相比单独使用for循环更简洁
#引申的也有字典推导式、集合推导式
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list = [i for i in a if i%2!=0]
# print(list)

'''
26、正则re.complie作用
'''
#编译一个正则表达式，返回一个正则表达式对象，方便后续代码的调用，用于提供给match和search函数

'''
# 27、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
'''
# #
# a=(1,)
# b=(1)
# c=("1")
# print(a)
# print(b)
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))

'''
# 28、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
'''
# list1 = [1,5,7,9]
# list2 = [2,2,6,8]
#方法一：列表相加，再进行排序
# list3 = list1+list2
# list3.sort(reverse=False)
# print(list3)
#方法二：zip函数,再进行降维
# list3 = list(zip(list1,list2))
# print(list3)

'''
# 29、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳
'''
#
# import datetime
# try:
#     print(datetime.date.today())
#     raise Exception("go to error")
# except Exception as result:
#     print('{0} {1} error occurred'.format(datetime.datetime.now().strftime('%y+%m+%d %H-%M:%S')+'星期'+str(datetime.datetime.today().isoweekday()),result))


'''
# 30、写一段自定义异常代码
'''
#方法一：直接使用try-except语句
#
# try:
#     x=1
#     y=3
#     print(x/y)
#     raise Exception('custom error')
# except Exception as result:
#     print(result)
#     print('error occured')
# else:
#     print('no error occur')
# finally:
#     print('calculate finished')
#
#方法二：继承exception基类
#
# class Myexception(Exception):
#     def __init__(self,message):
#         self.message=message
#
# try:
#     x = int(input('input:'))
#     if x < 0:
#         raise Myexception('to small')
# except Myexception as e:
#     print("myexception occur")

'''
# 31、正则表达式匹配中，（.*）和（.*?）匹配区别？
'''
#.匹配任意字符 *匹配0次或多次 ？匹配0次或1次
#.*贪婪匹配  .*?非贪婪匹配 每一次尽可能少的匹配,遇到结尾段就切分
# import re
# string = 'ascdefg'
# a = re.compile('.*')
# b = re.compile('.*?')
# c = re.findall(a,string)
# d = re.findall(b,string)
# print(c)
# print(d)

# 32、简述Django的orm
#

'''
# 33、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
'''
# #使用列表推导式
# list = [[1,2],[3,4],[5,6]]
# print([j for i in list for j in i])

'''
# 34、x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
'''
#
# x="abc"
# y="def"
# z=["d","e","f"]
# print('_'.join(x))
# print(x.join(y))
# print(x.join(z))


'''
# 35、举例说明异常模块中try except else finally的相关意义
'''
#try中包含可能报差的代码，except出现异常时执行，else为不出错正常执行 finally为程序不管是否正常运行至结束，都需要执行


'''
# 36、举例说明zip（）函数用法
'''
#将两个list合并为一个个元组，长度向最短的列表看齐

'''
# 37、a="张明 98分"，用re.sub，将98替换为100
'''
# import re
# a = "张明 98分"
# a = re.sub('[0-9]+','100',a)
# print(a)

#
# 38、a="hello"和b="你好"编码成bytes类型
#


# 39、[1,2,3]+[4,5,6]的结果是多少？

'''
# 40、提高python运行效率的方法
'''
#减少使用循环，尽量使用c构建的python库，如numpy\pandas\scipy等

#
# 41、遇到bug如何处理
#
# 42、正则匹配，匹配日期2018-03-20
#
# 43、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]

'''
# 44、写一个单列模式
'''
#确保一个类只有一个实例存在
#优点：节约内存，多个实例化对象都指向一个内存地址；实例的属性都可以共用
#__new__为对象分配空间，返回对象引用；__init__对象初始化，返回实例属性

#方法一、模块导入from...import... as ....
#as定义不同名称的实例，最后print指向的内存地址是一致的
#方法二、__new__魔术方法实现
# class MusicPlayer(object):
#
#     # 记录第一个被创建对象的引用
#     instance = None
#     # 记录是否执行过初始化动作
#     init_flag = False
#
#     def __new__(cls, *args, **kwargs):
#
#         # 1. 判断类属性是否是空对象
#         if cls.instance is None:
#             # 2. 调用父类的方法，为第一个对象分配空间
#             cls.instance = super().__new__(cls)
#
#         # 3. 返回类属性保存的对象引用
#         return cls.instance
#
#     def __init__(self):
#
#         if not MusicPlayer.init_flag:
#             print("初始化音乐播放器")
#
#             MusicPlayer.init_flag = True
#
#
# # 创建多个对象
# player1 = MusicPlayer()
# print(player1)
#
# player2 = MusicPlayer()
# print(player2)
#
# class Demo():
#     instance = None
#     def __new__(cls,*args, **kwargs):
#         if cls.instance == None:
#             cls.instance = object.__new__(cls)
#             return cls.instance
#         else:
#             return cls.instance
#
#     def __init__(self):
#         self.num = 1
#
# demo1 = Demo()
# demo2 = Demo()
# print(demo1)
# print(demo2)

#
'''
# 45、保留两位小数
'''
# #方法一、round方法
# a = 0.123464876
# print(round(a,2))
# #方法二、formate格式化方法
# print("{:.2f}".format(a))
# #注：以上方法并不会修改a的精度

#
# 46、求三个方法打印结果
#


# 47、分别从前端、后端、数据库阐述web项目的性能优化
#
'''
48、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
'''
#
# dic={"name":"zs","age":18}
# dic.pop('name')
# # del dic["name"]
# print(dic)

# 49、计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]
#
# 50、简述同源策略
#
# 51、简述cookie和session的区别
#
# 52、简述多线程、多进程

'''
# 53、简述any()和all()方法
'''
#any、all类似于或和与的判断，any是结果中有一个为true即为true，all是结果中有一个false即为false
# import os
# a = [1,2,34,98]
# print('any result is {0}'.format(any(a)))
# print('all result is {0}'.format(all(a)))
# print(type(any))

'''
54、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
'''
# IOError:输入输出异常
# AttributeError:试图访问一个对象没有的属性
# ImportError：无法引入模块或包，基本是路径问题
# IndentationError：语法错误，代码没有正确的对齐
# IndexError：下标索引超出序列边界
# KeyError:试图访问你字典里不存在的键
# SyntaxError:Python代码逻辑语法出错，不能执行
# NameError:使用一个还未赋予对象的变量


'''
55、python中copy和deepcopy区别
'''
#对不可变数据类型copy，赋值、浅复制、深复制id都一样
a = '123445'
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print('a=%s'%a)
print('b=%s'%b)
print('c=%s'%c)

#对可变数据类型
list = [1,2,3]
list2 = copy.copy(list)
list3 = copy.deepcopy(list)
list4 = list
print('origin {0}'.format(id(list)))
print('copy {0}'.format(id(list2)))
list[0]=3
print(list2)
print('deepcopy {0}'.format(id(list3)))
list.append(4)
print(list3)
print(list)
print('= {0}'.format(id(list4)))
print(list4)

'''
# 56、列出几种魔法方法并简要介绍用途
'''
#魔法方法是对内置方法的重载，注：不是重写！！
class Mystr(str):
    #-> bool表示一种注释，说明函数返回的是bool类型；：也是种注释，说明建议传入的为一个object\Int\string，实际不影响结果传入错误的也不影响结果
    def __eq__(self, __x:str)-> bool:
        return len(self) == len(__x)

a = Mystr("123")
b = Mystr("457")
print(a==b)


# 57、C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？
#
# 58、请将[i for i in range(3)]改成生成器
#


# 59、a = "  hehheh  ",去除收尾空格
#
'''
60、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
'''
# list=[0,-1,3,-10,5,9]
# list3 = [sorted(list)]
# #sort返回对象为空
# list.sort(reverse=True)
# print(list)
# print(list3)


# import json
# with open(r'D:\asrcat\20230406_19523704\task_cfg.json')as fp:
#     print(json.load(fp))