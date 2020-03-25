#数据库查询
"""注意：数据库查询不需要提交事务"""

import sqlite3

con = sqlite3.connect(r"d:/python3/db_test/sqllite_db/first.db")
cur = con.cursor()

sql = "select * from t_person"
try:
    cur.execute(sql)
    #person_all = cur.fetchall()          #fetchall()方法为查询表中所有数据，返回列表
    person01 = cur.fetchone()             #fetchone()方法为查询表中单条数据，返回元组
    print(person01)
    """
    print(person_all)
    for i in person_all:
        print(i)
    """
except Exception as e:
    print(e)
    print("查询失败")
finally:
    cur.close()
    con.close()