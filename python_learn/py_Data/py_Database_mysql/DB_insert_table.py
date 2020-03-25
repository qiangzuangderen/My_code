#测试向表中插入数据
"""注意：插入失败需要回滚事务rollback()方法"""

import pymysql

con = pymysql.connect(host="localhost", user="root", password="flamingo801123", database="python_test01", port=3306)
cur = con.cursor()

insert_sql = """
                insert into t_student(sname,age,score) values(%s,%s,%s)      #插入数据的SQL语句格式：确认插入数据的字段名称，添加字段对应的占位符%s
"""
args = [("yang",39,88.5),("smallyang",6,90),("lin",35,55.8)]        #添加单个数据行用元组方式，添加多个数据行用列表方式，列表项为元组

try:
    cur.executemany(insert_sql,args)
    con.commit()
    print("插入数据成功")
except Exception as e:
    print(e)
    print("插入数据失败")
    con.rollback()
finally:
    cur.close()
    con.close()