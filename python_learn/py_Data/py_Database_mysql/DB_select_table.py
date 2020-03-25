#测试表中查询

import pymysql

con = pymysql.connect(host="localhost", user="root", password="flamingo801123", database="python_test01", port=3306)
cur = con.cursor()

select_sql = """select * from t_student"""

try:
    cur.execute(select_sql)
    student_all = cur.fetchall()      #查询表中所有数据以元组形式返回，元组的项以元组表示
    for student in student_all:
        print(student)
except Exception as e:
    print(e)
    print("查询表失败")
finally:
    cur.close()
    con.close()