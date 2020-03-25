#可调用方法__call__


class salaryAccont:

    def __call__(self,salary):    #在类外部可以类名对象直接调用
        print("工资计算：")
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//8
        return dict(yearSalary = yearSalary,monthSalary = salary,daySalary = daySalary,hourSalary = hourSalary)

s1 = salaryAccont()
print(s1(9000))
