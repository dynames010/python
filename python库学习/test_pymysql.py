import pymysql
'''
basic function test
'''
# #连接mysql
# conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='',charset='utf8',db='sda1')
# cursor = conn.cursor()
#
# #增,需commit
# cursor.execute("insert into L1 (id,uid) values(1,1)")
# conn.commit()
#
# #删
# cursor.execute("delete from L1 where id<2")
# conn.commit()
#
# #改
# cursor.execute("update L1 set id=250 where id=160")
# conn.commit()
#
# #查
# cursor.execute("select * from L1")
# #data = cursor.fetchone()   #值获取第一行
# data = cursor.fetchall()    #获取表中所有数据
# print(data)
#
# #关闭连接
# cursor.close()
# conn.close()

'''
创建用户管理系统，包括用户的注册和登录
在项目最开始时创建数据库和数据表
'''

def register():
    print("---------enter register mode-----------")
    print("input name:")
    name = str(input())
    print("input age:")
    age = input()
    #数据库提前做的操作：创建数据库 create database info_sys
    #创建数据表 create table L1(name varchar(10),age int)default charset=utf8;
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='info_sys')
    cursor = conn.cursor()
    cursor.execute('insert into L1(name,age) values("{}","{}")'.format(name,age))
    conn.commit()
    cursor.execute('select * from L1')
    data = cursor.fetchall()
    print(data)
    cursor.close()
    conn.close()

def login():
    print("---------enter login mode-----------")
    print("input your name")
    name = input()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='info_sys')
    cursor = conn.cursor()
    # sql = 'select name from L1 where name="{0}"'.format(name)
    # cursor.execute(sql)
    #会出现注入，使用execute方法替换
    cursor.execute("select * from L1 where name=%s",[name])  #用占位符%s代替
    #cursor.execute('select * from L1 where name=%(n1)s and age=%(n2)d',{"n1":name,"n2":age})
    #data = cursor.fetchall()   #获取到值为元组，元组嵌套元组，每个元组为一行的数据
    data = cursor.fetchone()
    #未获取到返回空
    if data:
        print('found ')
    else:
        print('none')
    cursor.close()
    conn.close()

def run():
    while(1):
        print("enter 1-注册 2-登录 3-退出")
        choice = input()
        if choice=='1':
            register()
        elif choice=='2':
            login()
        else:
            break

if __name__ == '__main__':
    run()