'''
创建表结构并编写相应的sql语句

id  int 不为空&自增&主键
name varchar(32)    不为空
password varchar(64)    不为空
gender char(1)  不为空，支持：男、女
email varchar(64)   可以为空
amount decimal(10,2)    不为空&默认值为0
ctime datetime  新增时间（可基于datetime模块实现）

-任意插入五条数据
-将id>3的所有人性别改为 男    update L1 set gender="男" where id>3;
-查询余额 amount>1000的所有用户  select amount from L1 where amount>1000;
-让每个人的余额在自己原基础上+1000     update L1 set id=id+1000;
-删除性别为男的所有数据
-通过python代码实现所有操作
'''

import pymysql
import datetime
# insert into L1 values("6","blue","12323","男","23233qq","1000.0","2020-11-12 11:11:11");
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='exercise1')
cursor = conn.cursor()

cursor.execute("update L1 set amount=amount+1000")
conn.commit()

cursor.execute("insert into L1(id,name,password,gender,email,amount,ctime) values('14','xx','aassdd','女','233@qq','2000',%s)",[datetime.datetime.now()])
conn.commit()

cursor.execute("select amount from L1 where amount>1500")

cursor.execute("select * from L1")
data = cursor.fetchall()
print(data)
print(type(data))