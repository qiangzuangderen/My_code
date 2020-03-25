#数据库中内容的修改和删除
"""流程：
1.导入模块；
2.创建数据库文件连接；
3.建立游标；
4.编写SQL语句，设置需要修改的对象的占位符和主键位置的占位符，删除命令设置主键占位符；
5.执行SQL语句execute()方法；
5.提交事务commit()方法，修改不成功事务回滚rollback()方法；
6.关闭游标
7.关闭数据库文件连接。
"""

import sqlite3

con = sqlite3.connect(r"d:/python3/db_test/sqllite_db/first.db")
cur = con.cursor()
select_sql = "select * from t_person"
delete_sql = "delete from t_person where pno=?"     #删除命令提供主键占位符
try:
    update_sql = "update t_person set pname=?,age=? where pno=?"
    cur.execute(update_sql,("Sun",39,1))
    cur.execute(delete_sql,(4,))           #当元组中的项只有1项时，需要在项后加上“,”
    con.commit()
    print("修改完成")
    cur.execute(select_sql)
    person_all = cur.fetchall()
    for person in person_all:
        print(person)
except Exception as e:
    print(e)
    print("修改失败")
    con.rollback()
finally:
    cur.close()
    con.close()
