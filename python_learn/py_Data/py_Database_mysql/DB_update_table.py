#测试修改、删除表中的数据

import pymysql

con = pymysql.connect("localhost", "root", "flamingo801123", "python_test01", 3306)
cur = con.cursor()
update_sql = """update t_student set sname=%s,age=%s where sno=%s"""
insert_sql = """insert into t_student(sname,age,score) values(%s,%s,%s)"""
delete_sql = """delete from t_student where sname=%s"""
select_sql = """select * from t_student"""
try:
    cur.execute(select_sql)
    student_old = cur.fetchall()
    for student in student_old:
        print(student)
    cur.execute(update_sql, ("sun",39,1))
    cur.execute(insert_sql, ("lin",6,99.3))
    cur.execute(delete_sql,("杨语棋",))
    con.commit()
    print("数据操作成功")
    cur.execute(select_sql)
    student_all = cur.fetchall()
    for student in student_all:
        no = student[0]
        name = student[1]
        age = student[2]
        score = student[3]
        print("no:",no,"name:",name,"age:",age,"score:",score)
except Exception as e:
    print(e)
    print("数据操作失败")
    con.rollback()
finally:
    cur.close()
    con.close()

