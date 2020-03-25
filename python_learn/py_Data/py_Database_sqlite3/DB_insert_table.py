#向表中插入数据
"""
流程：
1.导入模块；
2.创建连接，与表的数据库文件一致；
3.创建游标；
4.编写SQL语句；
5.执行SQL语句，execute()方法为插入1条数据，executemany()方法为插入多条数据，传递参数：(1)SQL语句；(2)数据的值；
6.提交事务：commit()方法，插入失败进行事务回滚，rollback()方法；
7.关闭游标，关闭连接。
"""
import sqlite3

con = sqlite3.connect(r"d:/python3/db_test/sqllite_db/first.db")
cur = con.cursor()

sql = "insert into t_person(pname,age) values(?,?)"    #values(?,?)表示创建占位符

try:
    #cur.execute(sql,("yang",33))
    cur.executemany(sql,[("ling",35),("smallyang",6),("呆瓜",33)])     #插入多条数据时，传参用列表表示，列表的项用元组表示
    con.commit()                   #事务提交
    print("插入数据成功")
except Exception as e:
    print(e)
    print("插入数据失败")
    con.rollback()             #事务回滚
finally:
    cur.close()
    con.close()