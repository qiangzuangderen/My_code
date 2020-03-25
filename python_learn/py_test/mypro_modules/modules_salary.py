#创建模块modules_salary,用于计算员工的薪酬

def yearSalary(monthsalary):

    """传入月薪，计算年薪"""

    return monthsalary*12

def monthSalary(daysalary):

    """传入日薪，计算月薪(月薪按照每月22.5天计算)"""

    return daysalary*22.5

if __name__=="__main__":
    print(monthSalary(300))