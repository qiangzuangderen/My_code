"""
创建表的流程：
1.导入sqlite3模块；
2.创建连接sqlite3.connect();
3.创建游标对象；
4.编写创建表的SQL语句；
5.执行SQL，execute()方法;
6.执行SQL;
7.关闭表。
"""

import sqlite3
"""创建数据库连接"""
con = sqlite3.connect(r"d:/python3/db_test/sqllite_db/first.db")
print(con)

"""创建游标，游标可视为一个指针，指向数据库中的逐条数据"""
cur = con.cursor()

"""创建表"""
sql = """create table t_person(
        pno INTEGER primary key autoincrement,
        pname VARCHAR not null,
        age INTEGER
        )"""

"""执行SQL"""
try:
    cur.execute(sql)
    print("表创建成功")
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    """关闭游标"""
    cur.close()
    """关闭连接"""
    con.close()

