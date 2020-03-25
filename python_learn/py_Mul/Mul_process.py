#测试子进程的调用，向子进程传递参数
"""导入模块，注意：大写Process"""
from multiprocessing import Process

def run_test(name,age,**kwargs):
    print("运行子进程…………,name:{0},age:{1}".format(name,age))
    print("字典：",kwargs)

if __name__=="__main__":
    print("运行主进程…………")
    p = Process(target=run_test,args=("yang",39),kwargs={"job":"coding"})    #注意：大写Process(),target指向子进程函数
    """调用子进程"""
    p.start()
