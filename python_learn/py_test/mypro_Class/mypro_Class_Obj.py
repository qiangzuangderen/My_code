#类对象分析

class Students:

    company = "ZTG"       #类属性
    count = 0             #类属性

    def __init__(self,name,score):
        self.name = name            #实例属性
        self.score = score          #实例属性
        Students.count += 1         #调用类属性

    def say_score(self):
        print("{0}公司的{1}的分数是{2}".format(Students.company,self.name,self.score))

s1 = Students("yang",60)
s2 = Students("ling",90)
s3 = Students("yang",100)
s1.say_score()
s2.say_score()
s3.say_score()
print("共创建了{0}个对象".format(Students.count))