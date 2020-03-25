#在mysql中创建表
"""流程：
1.导入pymasql模块；
2.创建数据库文件连接：关键字(host=数据库主机位置，本机为localhost,user="用户名",password="登录密码",database="mysql中需操作的数据库名称")；
3.创建游标；
4.编写SQL语句；
5.执行SQL语句execute()方法；
6.关闭游标，关闭连接。
"""

import pymysql

con = pymysql.connect(host="localhost", user="root", password="flamingo801123", database="python_test01", port=3306)
#print(con)
cur = con.cursor()
sql = """
        create table t_student(
        sno int primary key auto_increment,
        sname VARCHAR(30) not null,
        age int(4),
        score float(3,1)
        )"""

try:
    cur.execute(sql)
    print("表创建成功")
except Exception as e:
    print(e)
    print("表创建失败")
finally:
    cur.close()
    con.close()